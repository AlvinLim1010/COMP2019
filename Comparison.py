# Data Manipulation
import pandas as pd # for data manipulation
import numpy as np

# Sklearn
from sklearn.svm import SVR # for building SVR model
from sklearn.linear_model import LinearRegression # for building Linear Regression model
from sklearn.multioutput import MultiOutputRegressor # To make the output be independent to each other
from sklearn.model_selection import train_test_split # Split the training and testing data to do comparison
from sklearn.metrics import mean_squared_error, mean_absolute_error # To do comparison
from sklearn.neural_network import MLPRegressor

dataset = pd.read_excel('Excel Data FIle/1077-55P.xlsx')

# Getting dataset
X = dataset[['pH Reactor', 'COD F/mg/L', 'COD Eff/mg/L', 'BOD F/mg/L', 'BOD Eff/mg/L']].values
y = dataset[['CH4', 'CO2']].values

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create the Linear Regression SVR regressor
lr = LinearRegression()

# Create the Multioutput Regressor
multiOutputLR = MultiOutputRegressor(lr)

# Train the regressor
multiOutputLR = multiOutputLR.fit(X_train, y_train)

# Generate predictions for testing data
y_pred_LR = multiOutputLR.predict(X_test)

temp = [[7.5, 52426, 24966, 40802, 19022]]

# get prediction for new input
new_output = multiOutputLR.predict(temp)
# summarize input and output
print(temp, new_output)

score_LR = multiOutputLR.score(X_test,y_test)
print(f'Score for LR: {score_LR}')