from Orange.classification import KNNLearner as KNNClassification
from Orange.modelling import Fitter
from Orange.regression import KNNRegressionLearner

__all__ = ['KNNLearner']


class KNNLearner(Fitter):
    __fits__ = {'classification': KNNClassification,
                'regression': KNNRegressionLearner}
