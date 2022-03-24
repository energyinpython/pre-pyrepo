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

