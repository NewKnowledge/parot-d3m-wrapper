# Parrot D3M Wrapper
Wrapper of the Parrot ARIMA primitive into D3M infrastructure. All code is written in Python 3.5 and must be run in 3.5 or greater. 

The base Sloth library (which also contains other methods that can be called on time series data) can be found here: https://github.com/NewKnowledge/sloth

## Install

pip3 install -e git+https://github.com/NewKnowledge/parrot-d3m-wrapper.git#egg=ParrotD3MWrapper --process-dependency-links

## Output
 The output is a list of length 'n_periods' that contains a prediction for each of 'n_periods' future time periods.

## Available Functions

#### set_training_data

Set's primitives training data. The input is a pandas data frame that contains training data in two columns. The first column contains time series indices (preferably in datetime format) and the second column contains time series values. There are no outputs. 

#### fit

Fits ARIMA model using trianing data from set_training_data and hyperparameters. There are no inputs or outputs. 

#### produce
Produce the primitive's prediction for future time series data. The output is a list of length 'n_periods' that contains a prediction for each of 'n_periods' future time periods. 'n_periods' is a hyperparameter that must be set before making the prediction.

