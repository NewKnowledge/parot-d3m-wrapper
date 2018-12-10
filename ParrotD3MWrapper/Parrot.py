import sys
import os.path
import numpy as np
import pandas
import typing
from typing import List

from Sloth import Sloth

from d3m.primitive_interfaces.base import PrimitiveBase, CallResult

from d3m import container, utils
from d3m.metadata import hyperparams, base as metadata_base, params

__author__ = 'Distil'
__version__ = '1.0.1'

Inputs = container.pandas.DataFrame
Outputs = container.List

class Params(params.Params):
    pass

class Hyperparams(hyperparams.Hyperparams):
    n_periods = hyperparams.UniformInt(lower = 1, upper = sys.maxsize, default = 18, semantic_types=[
       'https://metadata.datadrivendiscovery.org/types/TuningParameter'])
    seasonal = hyperparams.UniformBool(default = True, semantic_types = [
       'https://metadata.datadrivendiscovery.org/types/ControlParameter'],
       description="seasonal ARIMA prediction")
    seasonal_differencing = hyperparams.UniformInt(lower = 1, upper = 365, default = 12, 
        semantic_types=['https://metadata.datadrivendiscovery.org/types/TuningParameter'], 
        description='period of seasonal differencing')
    pass

class Parrot(PrimitiveBase[Inputs, Outputs, Params, Hyperparams]):
    metadata = metadata_base.PrimitiveMetadata({
        # Simply an UUID generated once and fixed forever. Generated using "uuid.uuid4()".
        'id': "d473d487-2c32-49b2-98b5-a2b48571e07c",
        'version': __version__,
        'name': "parrot",
        # Keywords do not have a controlled vocabulary. Authors can put here whatever they find suitable.
        'keywords': ['Time Series'],
        'source': {
            'name': __author__,
            'uris': [
                # Unstructured URIs.
                "https://github.com/NewKnowledge/parrot-d3m-wrapper",
            ],
        },
        # A list of dependencies in order. These can be Python packages, system packages, or Docker images.
        # Of course Python packages can also have their own dependencies, but sometimes it is necessary to
        # install a Python package first to be even able to run setup.py of another package. Or you have
        # a dependency which is not on PyPi.
         'installation': [{
             'type': metadata_base.PrimitiveInstallationType.PIP,
            'package': 'cython',
            'version': '0.28.5',
        },{
            'type': metadata_base.PrimitiveInstallationType.PIP,
            'package_uri': 'git+https://github.com/NewKnowledge/parrot-d3m-wrapper.git@{git_commit}#egg=ParrotD3MWrapper'.format(
                git_commit=utils.current_git_commit(os.path.dirname(__file__)),
            ),
        }],
        # The same path the primitive is registered with entry points in setup.py.
        'python_path': 'd3m.primitives.distil.parrot',
        # Choose these from a controlled vocabulary in the schema. If anything is missing which would
        # best describe the primitive, make a merge request.
        'algorithm_types': [
            metadata_base.PrimitiveAlgorithmType.AUTOREGRESSIVE_INTEGRATED_MOVING_AVERAGE,
        ],
        'primitive_family': metadata_base.PrimitiveFamily.TIME_SERIES_FORECASTING,
    })

    def __init__(self, *, hyperparams: Hyperparams, random_seed: int = 0)-> None:
        super().__init__(hyperparams=hyperparams, random_seed=random_seed)
        self._params = {}
        self._X_train = None        # training inputs
        self._arima = None          # ARIMA classifier
        self._sloth = Sloth()        # Sloth library 

    def fit(self) -> None:
        """
        Fits ARIMA model using training data from set_training_data and hyperparameters
        """

        # fits ARIMA model using training data from set_training_data and hyperparameters
        self._arima = self._sloth.FitSeriesARIMA(self._X_train, 
                                                self.hyperparams['seasonal'],
                                                self.hyperparams['seasonal_differencing'])

    def get_params(self) -> Params:
        return self._params

    def set_params(self, *, params: Params) -> None:
        self.params = params

    def set_training_data(self, *, inputs: Inputs, outputs: Outputs) -> None:
        """
        Set primitive's training data

        Parameters
        ----------
        inputs : pandas data frame containing training data where first column contains dates and second column contains values
        
        """
        self.X_train = inputs

    def produce(self, *, inputs: Inputs, timeout: float = None, iterations: int = None) -> CallResult[Outputs]:
        """
        Produce primitive's prediction for future time series data

        Parameters
        ----------
        None

        Returns
        ----------
        Outputs
            The output is a list containing a forecast for each of the 'n_periods' future time periods
        """

        future_forecast = self._sloth.PredictSeriesARIMA(self._arima, self.hyperparams['n_periods'])
        print(future_forecast)
        return CallResult(future_forecast)

if __name__ == '__main__':
    client = Parrot(hyperparams={'n_periods':18, 'seasonal':True, 'seasonal_differencing':12})
    data = pandas.read_csv("Electronic_Production.csv",index_col=0)
    # select training data from csv
    train = data.loc['1985-01-01':'2016-12-01']
    client.set_training_data(inputs = train, outputs = None)
    client.fit()
    results = client.produce()
    print(results)
