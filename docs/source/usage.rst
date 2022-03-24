Usage
=====

.. _installation:

Installation
------------

To use PyREPO, first install it using pip:

.. code-block:: console

   (.venv) $ pip install pyrepo

Importing methods from pyrepo package
-------------------------------------

MCDA methods for example TOPSIS:

>>> from pyrepo.mcda_methods import TOPSIS

weighting methods:

>>> from pyrepo import weighting_methods as mcda_weights

Normalization mathods:

>>> from pyrepo import normalizations as norms

Correlations:

>>> from pyrepo import correlations as corrs

Distance metrics:

>>> from pyrepo import distance_metrics as dists

Compromise rankings:

>>> from pyrepo import compromise_rankings as compromises

Sensitivity analysis method:

>>> from pyrepo.sensitivity_analysis import Sensitivity_analysis_weights

Ranking alternatives according to prefernce values:

>>> from pyrepo.additions import rank_preferences

