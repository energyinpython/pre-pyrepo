Welcome to PyREPO documentation!
===================================

PyREPO is Python 3 library for Multi-Criteria Decision Making.
This library includes:

- MCDA methods:

	- `TOPSIS`
	- `CODAS`
	- `MABAC`
	- `MULTIMOORA`
	- `VIKOR`
	- `WASPAS`
	- `EDAS`
	- `SPOTIS`
	
- Distance metrics:

	- `euclidean` (Euclidean distance)
	- `manhattan` (Manhattan distance)
	- `hausdorff` (Hausdorff distance)
	- `correlation` (Correlation distance)
	- `chebyshev` (Chebyshev distance)
	- `std_euclidean` (Standardized Euclidean distance)
	- `cosine` (Cosine distance)
	- `csm` (Cosine similarity measure)
	- `squared_euclidean` (Squared Euclidean distance)
	- `bray_curtis` (Sorensen or Bray-Curtis distance)
	- `canberra` (Canberra distance)
	- `lorentzian` (Lorentzian distance)
	- `jaccard` (Jaccard distance)
	- `dice` (Dice distance)
	- `bhattacharyya` (Bhattacharyya distance)
	- `hellinger` (Hellinger distance)
	- `matusita` (Matusita distance)
	- `squared_chord` (Squared-chord distance)
	- `pearson_chi_square` (Pearson chi square distance)
	- `squared_chi_square` (Sqaured chi square distance)
	
- Correlation coefficients:

	- `spearman` (Spearman rank correlation coefficient)
	- `weighted_spearman` (Weighted Spearman rank correlation coefficient)
	- `pearson_coeff` (Pearson correlation coefficient)
	- `WS_coeff` (Similarity rank coefficent - WS coefficient)
	
- Methods for normalization of decision matrix:

	- `linear_normalization` (Linear normalization)
	- `minmax_normalization` (Minimum-Maximum normalization)
	- `max_normalization` (Maximum normalization)
	- `sum_normalization` (Sum normalization)
	- `vector_normalization` (Vector normalization)
	- `multimoora_normalization` (Normalization method dedicated for the MULTIMOORA method)
	
- Methods for determination of criteria weights (weighting methods):

	- `entropy_weighting` (Entropy weighting method)
	- `std_weighting` (Standard Deviation weighting method)
	- `critic_weighting` (CRITIC weighting method)
	
- Methods for determination of compromise rankings based on several rankings obtained with different MCDA methods:

	- `borda_copeland_compromise_ranking` (Borda count and Copeland Method for compromise ranking)
	- `dominance_directed_graph` (Dominance Directed Graph for compromise ranking)
	- `rank_position_method` (Rank Position Method for compromise ranking)
	- `improved_borda_rule` (Improved Borda Rule method for compromise for MULTIMOORA method)
	
- Sensitivity analysis methods:

	- `Sensitivity_analysis_weights` (Methods for sensitivity analysis considering criteria weights modification)
	
- additions:

	- `rank_preferences` (Method for ordering alternatives according to their preference values obtained with MCDA methods)
	
Check out the :doc:`usage` section for further information, including
how to :ref:`installation` the project.

.. note::

   This project is under active development.

Contents
--------

.. toctree::

   usage
   api
