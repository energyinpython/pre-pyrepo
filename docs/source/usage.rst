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
	# Generate ranking of alternatives by sorting alternatives descendingly according to the TOPSIS algorithm (reverse = True means sorting in descending order) according to preference values
	rank = rank_preferences(pref, reverse = True)
	
	
The SPOTIS method

.. code-block:: console

	# provide decision matrix in array numpy.darray
	matrix = np.array([[15000, 4.3, 99, 42, 737],
	 [15290, 5.0, 116, 42, 892],
	 [15350, 5.0, 114, 45, 952],
	 [15490, 5.3, 123, 45, 1120]])

	# provide criteria weights in array numpy.darray. All weights must sum to 1.
	weights = np.array([0.2941, 0.2353, 0.2353, 0.0588, 0.1765])
	
	# provide criteria types in array numpy.darray. Profit criteria are represented by 1 and cost criteria by -1.
	types = np.array([-1, -1, -1, 1, 1])
	
	# Determine minimum bounds of performance values for each criterion in decision matrix
	bounds_min = np.array([14000, 3, 80, 35, 650])
	
	# Determine maximum bounds of performance values for each criterion in decision matrix
	bounds_max = np.array([16000, 8, 140, 60, 1300])
	
	# Stack minimum and maximum bounds vertically using vstack. You will get a matrix that has two rows and a number of columns equal to the number of criteria
	bounds = np.vstack((bounds_min, bounds_max))

	# Create the SPOTIS method object
	spotis = SPOTIS()
	# Calculate the SPOTIS preference values of alternatives
	pref = spotis(matrix, weights, types, bounds)
	# Generate ranking of alternatives by sorting alternatives ascendingly according to the SPOTIS algorithm (reverse = False means sorting in ascending order) according to preference values
	rank = rank_preferences(pref, reverse = False)
	

The Borda count and Copeland Method for compromise ranking

.. code-block:: console

	# Provide matrix with different rankings given by different MCDA methods in columns
	matrix = np.array([[7, 8, 7, 6, 7, 7],
	[4, 7, 5, 7, 5, 4],
	[8, 9, 8, 8, 9, 8],
	[1, 4, 1, 1, 1, 1],
	[2, 2, 2, 4, 3, 2],
	[3, 1, 4, 3, 2, 3],
	[10, 5, 10, 9, 8, 10],
	[6, 3, 6, 5, 4, 6],
	[9, 10, 9, 10, 10, 9],
	[5, 6, 3, 2, 6, 5]])
	
	# Calculate the compromise ranking using `borda_copeland_compromise_ranking` method
	result = compromises.borda_copeland_compromise_ranking(matrix)

