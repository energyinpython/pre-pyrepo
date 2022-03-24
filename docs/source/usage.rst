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

Import MCDA methods from module `mcda_methods`:

>>> from pyrepo.mcda_methods import CODAS, TOPSIS, WASPAS, VIKOR, SPOTIS, EDAS, MABAC, MULTIMOORA

Import weighting methods from module `weighting_methods`:

>>> from pyrepo import weighting_methods as mcda_weights

Import normalization methods from module `normalizations`:

>>> from pyrepo import normalizations as norms

Import correlation coefficient from module `correlations`:

>>> from pyrepo import correlations as corrs

Import distance metrics from module `distance_metrics`:

>>> from pyrepo import distance_metrics as dists

Import compromise rankings methods from module `compromise_rankings`:

>>> from pyrepo import compromise_rankings as compromises

Import Sensitivity analysis method from module `sensitivity_analysis`:

>>> from pyrepo.sensitivity_analysis import Sensitivity_analysis_weights

Import method for ranking alternatives according to prefernce values from module `additions`:

>>> from pyrepo.additions import rank_preferences


Usage examples
----------------------

The TOPSIS method

.. code-block:: console

	# provide decision matrix in array numpy.darray
	matrix = np.array([[256, 8, 41, 1.6, 1.77, 7347.16],
        [256, 8, 32, 1.0, 1.8, 6919.99],
        [256, 8, 53, 1.6, 1.9, 8400],
        [256, 8, 41, 1.0, 1.75, 6808.9],
        [512, 8, 35, 1.6, 1.7, 8479.99],
        [256, 4, 35, 1.6, 1.7, 7499.99]])

	# provide criteria weights in array numpy.darray. All weights must sum to 1.
	weights = np.array([0.405, 0.221, 0.134, 0.199, 0.007, 0.034])
	
	# provide criteria types in array numpy.darray. Profit criteria are represented by 1 and cost criteria by -1.
	types = np.array([1, 1, 1, 1, -1, -1])

	# Create the TOPSIS method object providing normalization method and distance metric
	topsis = TOPSIS(normalization_method = norms.minmax_normalization, distance_metric = distance_metric)
	# Calculate the TOPSIS preference values of alternatives
	pref = topsis(matrix, weights, types)
	# Generate ranking of alternatives by sorting alternatives descendingly according to TOPSIS algorithm (reverse = True means sorting in descending order) according to preference values
	rank = rank_preferences(pref, reverse = True)

