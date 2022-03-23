import numpy as np
import pandas as pd
import itertools

from .additions import rank_preferences
from .normalizations import *


# Borda count and Copeland Method for compromise ranking
def borda_copeland_compromise_ranking(matrix):
    """Calculate the compromise ranking considering several rankings obtained using different
    methods using Borda count and Copeland compromise ranking methodology

    Parameters
    ----------
        matrix : ndarray
            two-dimensional matrix containing different rankings in columns

    Returns
    -------
        ndarray
            vector including compromise ranking
    """

    grade_matrix = matrix.shape[0] - matrix
    wins_score = np.sum(grade_matrix, axis = 1)
    lossess_score = np.sum(wins_score) - wins_score
    rank = rank_preferences(wins_score - lossess_score, reverse = True)
    return rank


# Dominance Directed Graph for compromise ranking
def dominance_directed_graph(matrix):
    """Calculate the compromise ranking considering several rankings obtained using different
    methods using Dominance Directed Graph methodology

    Parameters
    ----------
        matrix : ndarray
            two-dimensional matrix containing different rankings in columns

    Returns
    -------
        ndarray
            vector including compromise ranking
    """

    m, n = matrix.shape
    A = np.zeros((m, m))
    for j, i in itertools.product(range(n), range(m)):
        ind_better = np.where(matrix[i, j] < matrix[:, j])[0]
        A[i, j] += len(ind_better)
    AS = np.sum(A, axis = 1)
    ASR = rank_preferences(AS, reverse = True)
    return ASR


# Rank Position Method for compromise ranking
def rank_position_method(matrix):
    """Calculate the compromise ranking considering several rankings obtained using different
    methods using Rank Position Method

    Parameters
    ----------
        matrix : ndarray
            two-dimensional matrix containing different rankings in columns

    Returns
    -------
        ndarray
            vector including compromise ranking
    """

    A = 1 / (np.sum((1 / matrix), axis = 1))
    RPM = rank_preferences(A, reverse = False)
    return RPM


# Improved Borda Rule method for compromise for MULTIMOORA
def improved_borda_rule(prefs, ranks):
    """Calculate the compromise ranking considering several rankings obtained using different
    methods using Improved Borda rule methodology

    Parameters
    ----------
        prefs : ndarray
            two-dimensional matrix containing preferences calculated by different methods in columns

        ranks : ndarray
            two-dimensional matrix containing rankings determined by different methods in columns

    Returns
    -------
        ndarray
            vector including compromise ranking
    """

    m, n = ranks.shape
    nprefs = multimoora_normalization(prefs, np.ones(n))
    A = (nprefs[:, 0] * ((m - ranks[:, 0] + 1) / (m * (m + 1) / 2))) - \
    (nprefs[:, 1] * (ranks[:, 1] / (m * (m + 1) / 2))) + \
    (nprefs[:, 2] * ((m - ranks[:, 2] + 1) / (m * (m + 1) / 2)))
    IMB = rank_preferences(A, reverse = True)
    return IMB