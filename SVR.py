# Data Manipulation
import pandas as pd # for data manipulation
import numpy as np # for data manipulation

# Sklearn
from sklearn.svm import SVR # for building SVR model
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

# Create the SVR regressor
svr = SVR(kernel='rbf', C=100, epsilon=1)

# Create the Multioutput Regressor
multiOutput = MultiOutputRegressor(svr)

# Train the regressor
multiOutput = multiOutput.fit(X_train, y_train)

# Generate predictions for testing data
y_pred = multiOutput.predict(X_test)

# Evaluate the regressor
mse_one = mean_squared_error(y_test[:,0], y_pred[:,0])
mse_two = mean_squared_error(y_test[:,1], y_pred[:,1])
mse_three = mean_squared_error(y_test[:,2], y_pred[:,2])
print(f'MSE for first regressor: {mse_one} - second regressor: {mse_two} - third regressor: {mse_three}')
mae_one = mean_absolute_error(y_test[:,0], y_pred[:,0])
mae_two = mean_absolute_error(y_test[:,1], y_pred[:,1])
mae_three = mean_absolute_error(y_test[:,2], y_pred[:,2])
print(f'MAE for first regressor: {mae_one} - second regressor: {mae_two}  third regressor: {mae_three}')