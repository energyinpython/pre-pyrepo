import numpy as np
from pyrepo import correlations as corrs

# Provide two vectors with rankings obtained with different MCDA methods
R = np.array([1, 2, 3, 4, 5])
Q = np.array([1, 3, 2, 4, 5])

# Calculate the compromise ranking using `pearson_coeff` coefficient
coeff = corrs.pearson_coeff(R, Q)
print('Pearson coeff: ', np.round(coeff, 4))