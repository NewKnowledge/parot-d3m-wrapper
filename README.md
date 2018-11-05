# Parrot D3M Wrapper
Parrot - Predictive AutoRegressive Results On Time

This library is a wrapper of Sloth's ARIMA time series prediction function into the D3M infrastructure. Code is written in Python 3.6 and must be run in Python 3.6 or greater. 

## Input

The input is a pandas data frame that contains training data in two columns. The first column contains time series indices (preferably in datetime format) and the second column contains time series values. 

## Output 

The output is a list of length 'n_periods' that contains a prediction for each of 'n_periods' future time periods. 'n_periods' is a hyperparameter that must be set before making the prediction.

## Available Functions

#### produce
Produce the primitive's prediction for future time series data. The input is a pandas data frame, with characteristics described above. The output is a list of length 'n_periods'.
>>>>>>> 7e0f21d74e6c0c09576a7704756285c69922c928
=======
# parrot-d3m-wrapper
Parrot - Predictive AutoRegressive Results on Time
>>>>>>> parent of 9faaf32... version 1.0.0 of shallot d3m wrapper
