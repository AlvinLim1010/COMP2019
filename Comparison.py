# Data Manipulation
import pandas as pd # for data manipulation
import numpy as np # for data manipulation

# Sklearn
from sklearn.svm import SVR # for building SVR model
from sklearn.linear_model import LinearRegression # for building Linear Regression model
from sklearn.datasets import make_regression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler


# Generate dataset
X, y = make_regression(n_samples=25000, n_features=3, n_targets=3, random_state=0)

#Standardized and Normalized the dataset
sc_X = StandardScaler()
sc_y = StandardScaler()

X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# Create the Linear Regression SVR regressor
lr = LinearRegression()
svr = SVR(kernel='rbf', C=100, epsilon=1)

# Create the Multioutput Regressor
multiOutputLR = MultiOutputRegressor(lr)
multiOutputSVR = MultiOutputRegressor(svr)

# Train the regressor
multiOutputLR = multiOutputLR.fit(X_train, y_train)
multiOutputSVR = multiOutputSVR.fit(X_train, y_train)

# Generate predictions for testing data
y_pred_LR = multiOutputLR.predict(X_test)
y_pred_SVR = multiOutputSVR.predict(X_test)

# Evaluate the regressor
mse_one_LR = mean_squared_error(y_test[:,0], y_pred_LR[:,0])
mse_two_LR = mean_squared_error(y_test[:,1], y_pred_LR[:,1])
mse_three_LR = mean_squared_error(y_test[:,2], y_pred_LR[:,2])
print(f'MSE for first LR regressor: {mse_one_LR} - second LR regressor: {mse_two_LR} - third LR regressor: {mse_three_LR}')
mae_one_LR = mean_absolute_error(y_test[:,0], y_pred_LR[:,0])
mae_two_LR = mean_absolute_error(y_test[:,1], y_pred_LR[:,1])
mae_three_LR = mean_absolute_error(y_test[:,2], y_pred_LR[:,2])
print(f'MAE for first LR regressor: {mae_one_LR} - second LR regressor: {mae_two_LR}  third LR regressor: {mae_three_LR}')

mse_one_SVR = mean_squared_error(y_test[:,0], y_pred_SVR[:,0])
mse_two_SVR = mean_squared_error(y_test[:,1], y_pred_SVR[:,1])
mse_three_SVR = mean_squared_error(y_test[:,2], y_pred_SVR[:,2])
print(f'MSE for first SVR regressor: {mse_one_SVR} - second SVR regressor: {mse_two_SVR} - third SVR regressor: {mse_three_SVR}')
mae_one_SVR = mean_absolute_error(y_test[:,0], y_pred_SVR[:,0])
mae_two_SVR = mean_absolute_error(y_test[:,1], y_pred_SVR[:,1])
mae_three_SVR = mean_absolute_error(y_test[:,2], y_pred_SVR[:,2])
print(f'MAE for first SVR regressor: {mae_one_SVR} - second SVR regressor: {mae_two_SVR}  third SVR regressor: {mae_three_SVR}')