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

Parameters
	matrix : ndarray
		Decision matrix with m alternatives in rows and n criteria in columns
	weights : ndarray
		Vector with criteria weights
	types : ndarray
		Vector with criteria types
		
Returns
	ndarray
		Vector with preference values of alternatives. Alternatives have to be ranked in descending order according to preference values.

::

	import numpy as np
	from pyrepo.mcda_methods import TOPSIS
	from pyrepo import normalizations as norms
	from pyrepo import distance_metrics as dists
	from pyrepo.additions import rank_preferences

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

	# Create the TOPSIS method object providing normalization method and distance metric.
	
	topsis = TOPSIS(normalization_method = norms.minmax_normalization, distance_metric = dists.euclidean)

	# Calculate the TOPSIS preference values of alternatives
	
	pref = topsis(matrix, weights, types)

	# Generate ranking of alternatives by sorting alternatives descendingly according to the TOPSIS algorithm (reverse = True means sorting in descending order) according to preference values
	
	rank = rank_preferences(pref, reverse = True)

	print('Preference values: ', pref)
	print('Ranking: ', rank)
	
Output

.. code-block:: console

	Preference values:  [0.4242 0.3217 0.4453 0.3353 0.8076 0.2971]
	Ranking:  [3 5 2 4 1 6]

	
	
The VIKOR method

Parameters
	matrix : ndarray
		Decision matrix with m alternatives in rows and n criteria in columns
	weights : ndarray
		Vector with criteria weights
	types : ndarray
		Vector with criteria types
		
Returns
	ndarray
		Vector with preference values of alternatives. Alternatives have to be ranked in ascending order according to preference values.

.. code-block:: console

	import numpy as np
	from pyrepo.mcda_methods import VIKOR

	# provide decision matrix in array numpy.darray
	matrix = np.array([[8, 7, 2, 1],
	[5, 3, 7, 5],
	[7, 5, 6, 4],
	[9, 9, 7, 3],
	[11, 10, 3, 7],
	[6, 9, 5, 4]])

	# provide criteria weights in array numpy.darray. All weights must sum to 1.
	weights = np.array([0.4, 0.3, 0.1, 0.2])
	
	# provide criteria types in array numpy.darray. Profit criteria are represented by 1 and cost criteria by -1.
	types = np.array([1, 1, 1, 1])

	# Create the VIKOR method object providing v parameter. The default v parameter is set to 0.5, so if you do not provide it, v will be equal to 0.5.
	vikor = VIKOR(v = 0.625)
	
	# Calculate the VIKOR preference values of alternatives
	pref = vikor(matrix, weights, types)
	
	# Generate ranking of alternatives by sorting alternatives ascendingly according to the VIKOR algorithm (reverse = False means sorting in ascending order) according to preference values
	rank = rank_preferences(pref, reverse = False)
	
	print('Preference values: ', pref)
	print('Ranking: ', rank)
	
Output

.. code-block:: console

	Preference values:  [0.6399 1.     0.6929 0.2714 0.     0.6939]
	Ranking:  [3 6 4 2 1 5]
	

	
The SPOTIS method

Parameters
	matrix : ndarray
		Decision matrix with m alternatives in rows and n criteria in columns
	weights : ndarray
		Vector with criteria weights
	types : ndarray
		Vector with criteria types
		
Returns
	ndarray
		Vector with preference values of alternatives. Alternatives have to be ranked in ascending order according to preference values.

.. code-block:: console

	import numpy as np
	from pyrepo.mcda_methods import SPOTIS

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
	
	print('Preference values: ', pref)
	print('Ranking: ', rank)
	
Output

.. code-block:: console

	Preference values:  [0.478  0.5781 0.5557 0.5801]
	Ranking:  [1 3 2 4]

	
	
The CODAS method

Parameters
	matrix : ndarray
		Decision matrix with m alternatives in rows and n criteria in columns
	weights : ndarray
		Vector with criteria weights
	types : ndarray
		Vector with criteria types
		
Returns
	ndarray
		Vector with preference values of alternatives. Alternatives have to be ranked in descending order according to preference values.

.. code-block:: console

	import numpy as np
	from pyrepo.mcda_methods import CODAS

	# provide decision matrix in array numpy.darray
	matrix = np.array([[45, 3600, 45, 0.9],
	[25, 3800, 60, 0.8],
	[23, 3100, 35, 0.9],
	[14, 3400, 50, 0.7],
	[15, 3300, 40, 0.8],
	[28, 3000, 30, 0.6]])

	# provide criteria weights in array numpy.darray. All weights must sum to 1.
	weights = np.array([0.2857, 0.3036, 0.2321, 0.1786])
	
	# provide criteria types in array numpy.darray. Profit criteria are represented by 1 and cost criteria by -1.
	types = np.array([1, -1, 1, 1])

	# Create the CODAS method object providing normalization method (in CODAS it is linear_normalization by default), distance metric, and tau parameter, which is equal to 0.02 default. tau must be in the range from 0.01 to 0.05.
	codas = CODAS(normalization_method = norms.linear_normalization, distance_metric = dists.euclidean, tau = 0.02)
	
	# Calculate the CODAS preference values of alternatives
	pref = codas(matrix, weights, types)
	
	# Generate ranking of alternatives by sorting alternatives descendingly according to the CODAS algorithm (reverse = True means sorting in descending order) according to preference values
	rank = rank_preferences(pref, reverse = True)
	
	print('Preference values: ', pref)
	print('Ranking: ', rank)
	
Output

.. code-block:: console

	Preference values:  [ 1.3914  0.3411 -0.217  -0.5381 -0.7292 -0.2481]
	Ranking:  [1 2 3 5 6 4]

	
	
The WASPAS method

Parameters
	matrix : ndarray
		Decision matrix with m alternatives in rows and n criteria in columns
	weights : ndarray
		Vector with criteria weights
	types : ndarray
		Vector with criteria types
		
Returns
	ndarray
		Vector with preference values of alternatives. Alternatives have to be ranked in descending order according to preference values.

.. code-block:: console

	import numpy as np
	from pyrepo.mcda_methods import WASPAS

	# provide decision matrix in array numpy.darray
	matrix = np.array([[5000, 3, 3, 4, 3, 2],
	[680, 5, 3, 2, 2, 1],
	[2000, 3, 2, 3, 4, 3],
	[600, 4, 3, 1, 2, 2],
	[800, 2, 4, 3, 3, 4]])

	# provide criteria weights in array numpy.darray. All weights must sum to 1.
	weights = np.array([0.157, 0.249, 0.168, 0.121, 0.154, 0.151])
	
	# provide criteria types in array numpy.darray. Profit criteria are represented by 1 and cost criteria by -1.
	types = np.array([-1, 1, 1, 1, 1, 1])

	# Create the WASPAS method object providing normalization method (in WASAPS it is linear_normalization by default), and lambda parameter, which is equal to 0.5 default. tau must be in the range from 0 to 1.
	waspas = WASPAS(normalization_method=norms.linear_normalization, lambda_param=0.5)
	
	# Calculate the WASPAS preference values of alternatives
	pref = waspas(matrix, weights, types)
	
	# Generate ranking of alternatives by sorting alternatives descendingly according to the WASPAS algorithm (reverse = True means sorting in descending order) according to preference values
	rank = rank_preferences(pref, reverse = True)
	
	print('Preference values: ', pref)
	print('Ranking: ', rank)
	
Output

.. code-block:: console

	Preference values:  [0.5623 0.6578 0.6193 0.641  0.7224]
	Ranking:  [5 2 4 3 1]

	
	
The EDAS method

Parameters
	matrix : ndarray
		Decision matrix with m alternatives in rows and n criteria in columns
	weights : ndarray
		Vector with criteria weights
	types : ndarray
		Vector with criteria types
		
Returns
	ndarray
		Vector with preference values of alternatives. Alternatives have to be ranked in descending order according to preference values.

.. code-block:: console

	import numpy as np
	from pyrepo.mcda_methods import EDAS

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

	# Create the EDAS method object.
	edas = EDAS()
	
	# Calculate the EDAS preference values of alternatives
	pref = edas(matrix, weights, types)
	
	# Generate ranking of alternatives by sorting alternatives descendingly according to the EDAS algorithm (reverse = True means sorting in descending order) according to preference values
	rank = rank_preferences(pref, reverse = True)
	
	print('Preference values: ', pref)
	print('Ranking: ', rank)
	
Output

.. code-block:: console

	Preference values:  [0.4141 0.13   0.4607 0.212  0.9443 0.043 ]
	Ranking:  [3 5 2 4 1 6]

	
	
The MABAC method

Parameters
	matrix : ndarray
		Decision matrix with m alternatives in rows and n criteria in columns
	weights : ndarray
		Vector with criteria weights
	types : ndarray
		Vector with criteria types
		
Returns
	ndarray
		Vector with preference values of alternatives. Alternatives have to be ranked in descending order according to preference values.

.. code-block:: console

	import numpy as np
	from pyrepo.mcda_methods import MABAC

	# provide decision matrix in array numpy.darray
	matrix = np.array([[2.937588, 2.762986, 3.233723, 2.881315, 3.015289, 3.313491],
	[2.978555, 3.012820, 2.929487, 3.096154, 3.012820, 3.593939],
	[3.286673, 3.464600, 3.746009, 3.715632, 3.703427, 4.133620],
	[3.322037, 3.098638, 3.262154, 3.147851, 3.206675, 3.798684],
	[3.354866, 3.270945, 3.221880, 3.213207, 3.670508, 3.785941],
	[2.796570, 2.983000, 2.744904, 2.692550, 2.787563, 2.878851],
	[2.846491, 2.729618, 2.789990, 2.955624, 3.123323, 3.646595],
	[3.253458, 3.208902, 3.678499, 3.580044, 3.505663, 3.954262],
	[2.580718, 2.906903, 3.176497, 3.073653, 3.264727, 3.681887],
	[2.789011, 3.000000, 3.101099, 3.139194, 2.985348, 3.139194],
	[3.418681, 3.261905, 3.187912, 3.052381, 3.266667, 3.695238]])

	# provide criteria weights in array numpy.darray. All weights must sum to 1.
	weights = np.array([0.171761, 0.105975, 0.191793, 0.168824, 0.161768, 0.199880])
	
	# provide criteria types in array numpy.darray. Profit criteria are represented by 1 and cost criteria by -1.
	types = np.array([1, 1, 1, 1, 1, 1])

	# Create the MABAC method object providing normalization method. In MABAC it is minmax_normalization by default.
	mabac = MABAC(normalization_method=norms.minmax_normalization)
	
	# Calculate the MABAC preference values of alternatives
	pref = mabac(matrix, weights, types)
	
	# Generate ranking of alternatives by sorting alternatives descendingly according to the MABAC algorithm (reverse = True means sorting in descending order) according to preference values
	rank = rank_preferences(pref, reverse = True)
	
	print('Preference values: ', pref)
	print('Ranking: ', rank)
	
Output

.. code-block:: console

	Preference values:  [-0.1553 -0.0895  0.5054  0.1324  0.2469 -0.3868 -0.1794  0.3629 -0.0842
	-0.1675  0.1399]
	Ranking:  [ 8  7  1  5  3 11 10  2  6  9  4]

	
	
The MULTIMOORA method

Parameters
	matrix : ndarray
		Decision matrix with m alternatives in rows and n criteria in columns
	weights : ndarray
		Vector with criteria weights
	types : ndarray
		Vector with criteria types
		
Returns
	ndarray
		Vector with preference values of alternatives. Alternatives have to be ranked in descending order according to preference values.

.. code-block:: console

	import numpy as np
	from pyrepo.mcda_methods import MULTIMOORA

	# provide decision matrix in array numpy.darray
	matrix = np.array([[4, 3, 3, 4, 3, 2, 4],
	[3, 3, 4, 3, 5, 4, 4],
	[5, 4, 4, 5, 5, 5, 4]])

	# provide criteria weights in array numpy.darray. All weights must sum to 1.
	weights = np.array([0.215, 0.215, 0.159, 0.133, 0.102, 0.102, 0.073])
	
	# provide criteria types in array numpy.darray. Profit criteria are represented by 1 and cost criteria by -1.
	types = np.array([1, 1, 1, 1, 1, 1, 1])

	# Create the MULTIMOORA method object providing compromise_rank_method. In MULTIMOORA it is dominance_directed_graph by default.
	multimoora = MULTIMOORA(compromise_rank_method = dominance_directed_graph)
	
	# Calculate the MULTIMOORA preference values of alternatives
	pref = multimoora(matrix, weights, types)
	
	# Generate ranking of alternatives by sorting alternatives descendingly according to the MULTIMOORA algorithm (reverse = True means sorting in descending order) according to preference values
	rank = rank_preferences(pref, reverse = True)
	
	print('Ranking: ', rank)
	
Output

.. code-block:: console

	Ranking:  [3 2 1]
	

	
Methods for determining compromise rankings
	
The Borda count and Copeland Method for compromise ranking

Parameters
	matrix : ndarray
		Matrix with rankings provided by different MCDA methods in particular columns.
		
Returns
	ndarray
		Vector with compromise ranking.

.. code-block:: console

	import numpy as np
	from pyrepo import compromise_rankings as compromises

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
	
	print('Copeland compromise ranking: ', result)
	
Output

.. code-block:: console

	Copeland compromise ranking:  [ 7  6  8  1  2  3  9  5 10  4]


	
The Dominance Directed Graph

Parameters
	matrix : ndarray
		Matrix with rankings provided by different MCDA methods in particular columns.
		
Returns
	ndarray
		Vector with compromise ranking.

.. code-block:: console

	import numpy as np
	from pyrepo import compromise_rankings as compromises

	# Provide matrix with different rankings given by different MCDA methods in columns
	matrix = np.array([[3, 2, 3],
	[2, 3, 2],
	[1, 1, 1]])
	
	# Calculate the compromise ranking using `dominance_directed_graph` method
	result = compromises.dominance_directed_graph(matrix)
	
	print('Dominance directed graph compromise ranking: ', result)
	
Output

.. code-block:: console

	Dominance directed graph compromise ranking:  [3 2 1]

	
	
The Rank Position compromise ranking method

Parameters
	matrix : ndarray
		Matrix with rankings provided by different MCDA methods in particular columns.
		
Returns
	ndarray
		Vector with compromise ranking.

.. code-block:: console

	import numpy as np
	from pyrepo import compromise_rankings as compromises

	# Provide matrix with different rankings given by different MCDA methods in columns
	matrix = np.array([[3, 2, 3],
	[2, 3, 2],
	[1, 1, 1]])
	
	# Calculate the compromise ranking using `rank_position_method` method
	result = compromises.rank_position_method(matrix)
	
	print('Rank position compromise ranking: ', result)
	
Output

.. code-block:: console

	Rank position compromise ranking:  [3 2 1]


	
The Improved Borda Rule compromise ranking method for MULTIMOORA

Parameters
	prefs : ndarray
		Matrix with preference values provided by different approaches of MULTIMOORA in particular columns.
	ranks : ndarray
		Matrix with rankings provided by different approaches of MULTIMOORA in particular columns.
		
Returns
	ndarray
		Vector with compromise ranking.

.. code-block:: console

	import numpy as np
	from pyrepo import compromise_rankings as compromises
	
	# Provide matrix with different preference values given by different MCDA methods in columns
	prefs = np.array([[4.94364901e-01, 4.56157867e-02, 3.85006756e-09],
	[5.26950959e-01, 6.08111832e-02, 9.62516889e-09],
	[6.77457681e-01, 0.00000000e+00, 4.45609671e-08]])

	# Provide matrix with different rankings given by different MCDA methods in columns
	matrix = np.array([[3, 2, 3],
	[2, 3, 2],
	[1, 1, 1]])
	
	# Calculate the compromise ranking using `improved_borda_rule` method
	result = compromises.improved_borda_rule(prefs, ranks)
	
    print('Improved Borda Rule compromise ranking: ', result)

Output

.. code-block:: console

	Improved Borda Rule compromise ranking:  [2 3 1]



Correlation coefficents

Spearman correlation coefficient

Parameters
	R : ndarray
		First vector containing values
	Q : ndarray
		Second vector containing values
		
Returns
	float
        Value of correlation coefficient between two vectors

.. code-block:: console

	import numpy as np
	from pyrepo import correlations as corrs

	# Provide two vectors with rankings obtained with different MCDA methods
	R = np.array([1, 2, 3, 4, 5])
    Q = np.array([1, 3, 2, 4, 5])
	
	# Calculate the compromise ranking using `spearman` coefficient
	coeff = corrs.spearman(R, Q)
	
Output

.. code-block:: console

	Spearman coeff:  0.9

	
	
Weighted Spearman correlation coefficient

Parameters
	R : ndarray
		First vector containing values
	Q : ndarray
		Second vector containing values
		
Returns
	float
        Value of correlation coefficient between two vectors

.. code-block:: console

	import numpy as np
	from pyrepo import correlations as corrs

	# Provide two vectors with rankings obtained with different MCDA methods
	R = np.array([1, 2, 3, 4, 5])
    Q = np.array([1, 3, 2, 4, 5])
	
	# Calculate the compromise ranking using `weighted_spearman` coefficient
	coeff = corrs.weighted_spearman(R, Q)
	
Output

.. code-block:: console

	Weighted Spearman coeff:  0.8833
	
	
	
Similarity rank coefficient WS

Parameters
	R : ndarray
		First vector containing values
	Q : ndarray
		Second vector containing values
		
Returns
	float
        Value of similarity coefficient between two vectors

.. code-block:: console

	import numpy as np
	from pyrepo import correlations as corrs

	# Provide two vectors with rankings obtained with different MCDA methods
	R = np.array([1, 2, 3, 4, 5])
    Q = np.array([1, 3, 2, 4, 5])
	
	# Calculate the compromise ranking using `WS_coeff` coefficient
	coeff = corrs.WS_coeff(R, Q)
	
Output

.. code-block:: console

	WS coeff:  0.8542

	
	
Pearson correlation coefficient

Parameters
	R : ndarray
		First vector containing values
	Q : ndarray
		Second vector containing values
		
Returns
	float
        Value of correlation coefficient between two vectors

.. code-block:: console

	import numpy as np
	from pyrepo import correlations as corrs

	# Provide two vectors with rankings obtained with different MCDA methods
	R = np.array([1, 2, 3, 4, 5])
    Q = np.array([1, 3, 2, 4, 5])
	
	# Calculate the compromise ranking using `pearson_coeff` coefficient
	coeff = corrs.pearson_coeff(R, Q)
	
Output

.. code-block:: console

	Pearson coeff:  0.9

	
	
Method for sensitivity analysis considering criteria weights modification

sensitivity_analysis

Parameters
	matrix : ndarray
		Decision matrix with alternatives performances data. This matrix includes
		data on m alternatives in rows considering criteria in columns
	weights : ndarray
		Vector with criteria weights. All weights in this vector must sum to 1.
	types : ndarray
		Vector with criteria types. Types can be equal to 1 for profit criteria and -1
		for cost criteria.
	percentages : ndarray
		Vector with percentage values of given criteria weight modification.
	mcda_name : str
		Name of applied MCDA method
	j : int
		Index of column in decision matrix `matrix` that indicates for which criterion
		the weight is modified. 
		
Returns
	data_sens : DataFrame
        dataframe with rankings calculated for subsequent modifications of criterion j weight

.. code-block:: console

	import numpy as np
	from pyrepo.sensitivity_analysis import Sensitivity_analysis_weights
	
	import numpy as np
	from pyrepo.mcda_methods import CODAS

	# provide decision matrix in array numpy.darray
	matrix = np.array([[45, 3600, 45, 0.9],
	[25, 3800, 60, 0.8],
	[23, 3100, 35, 0.9],
	[14, 3400, 50, 0.7],
	[15, 3300, 40, 0.8],
	[28, 3000, 30, 0.6]])

	# provide criteria weights in array numpy.darray. All weights must sum to 1.
	weights = np.array([0.2857, 0.3036, 0.2321, 0.1786])
	
	# provide criteria types in array numpy.darray. Profit criteria are represented by 1 and cost criteria by -1.
	types = np.array([1, -1, 1, 1])
	
	# provide vector with percentage values of chosen criterion weight modification
	percentages = np.arange(0.05, 0.5, 0.1)
	
	# provide mcda_name, for example 'SPOTIS' to apply the SPOTIS method
	mcda_name = 'SPOTIS'
	
	# provide index of j-th chosen criterion whose weight will be modified in sensitivity analysis, for example j = 1 for criterion in the second column
	j = 1
	
	# Create the Sensitivity_analysis_weights object
	sensitivity_analysis = Sensitivity_analysis_weights()

	# Generate DataFrame with rankings for different modification of weight of chosen criterion
	# Provide decision matrix `matrix`, vector with criteria weights `weights`, criteria types `types`, name of chosen MCDA method `mcda_name` and index of chosen criterion whose weight will be modified
	data_sens = sensitivity_analysis(matrix, weights, types, percentages, mcda_name, j)
	
