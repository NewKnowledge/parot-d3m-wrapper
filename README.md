# Parrot D3M Wrapper
Parrot - Predictive AutoRegressive Results On Time

This library is a wrapper of Sloth's ARIMA time series prediction function into the D3M infrastructure. Code is written in Python 3.6 and must be run in Python 3.6 or greater. 

## Available Functions

#### set_training_data

Set's primitives training data. The input is a pandas data frame that contains training data in two columns. The first column contains time series indices (preferably in datetime format) and the second column contains time series values. There are no outputs. 

#### fit

Fits ARIMA model using trianing data from set_training_data and hyperparameters. There are no inputs or outputs. 

#### produce
Produce the primitive's prediction for future time series data. The output is a list of length 'n_periods' that contains a prediction for each of 'n_periods' future time periods. 'n_periods' is a hyperparameter that must be set before making the prediction.

