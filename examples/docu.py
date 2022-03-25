import numpy as np
from pyrepo import normalizations as norms

def main():

    matrix = np.array([[8, 7, 2, 1],
    [5, 3, 7, 5],
    [7, 5, 6, 4],
    [9, 9, 7, 3],
    [11, 10, 3, 7],
    [6, 9, 5, 4]])

    types = np.array([1, 1, 1, 1])

    norm_matrix = norms.vector_normalization(matrix, types)
    print('Normalized matrix: ', np.round(norm_matrix, 4))


if __name__ == '__main__':
    main()