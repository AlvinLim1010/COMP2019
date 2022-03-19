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
from sklearn.preprocessing import StandardScaler # Standardized and normalized the x and y data

dataset = pd.read_excel('Data_SEGP.xlsx')
dataset.drop("Unnamed: 18", axis=1, inplace=True)
dataset.drop("Unnamed: 19", axis=1, inplace=True)
dataset.drop("Unnamed: 20", axis=1, inplace=True)
dataset.drop("Unnamed: 21", axis=1, inplace=True)
print(dataset.isnull().sum())

updated_df = dataset
updated_df['CH4'] = updated_df['CH4'].fillna(updated_df['CH4'].median()).round(1)
updated_df['Volume Biogas/L'] = updated_df['Volume Biogas/L'].fillna(updated_df['Volume Biogas/L'].median()).round(1)
updated_df['H2S'] = updated_df['H2S'].fillna(updated_df['H2S'].median()).round(1)
updated_df['CO2'] = updated_df['CO2'].fillna(updated_df['CO2'].median()).round(1)
updated_df['pH Reactor'] = updated_df['pH Reactor'].fillna(updated_df['pH Reactor'].median()).round(1)
updated_df['pH F'] = updated_df['pH F'].fillna(updated_df['pH F'].median()).round(1)
updated_df['pH Eff'] = updated_df['pH Eff'].fillna(updated_df['pH Eff'].median()).round(1)
updated_df['ORL gCOD/Ld'] = updated_df['ORL gCOD/Ld'].fillna(updated_df['ORL gCOD/Ld'].median()).round(1)
updated_df['COD F/mg/L'] = updated_df['COD F/mg/L'].fillna(updated_df['COD F/mg/L'].median()).round(1)
updated_df['COD Eff/mg/L'] = updated_df['COD Eff/mg/L'].fillna(updated_df['COD Eff/mg/L'].median()).round(1)
updated_df['COD removal'] = updated_df['COD removal'].fillna(updated_df['COD removal'].median()).round(1)
updated_df['BOD F/mg/L'] = updated_df['BOD F/mg/L'].fillna(updated_df['BOD F/mg/L'].median()).round(1)
updated_df['BOD Eff/mg/L'] = updated_df['BOD Eff/mg/L'].fillna(updated_df['BOD Eff/mg/L'].median()).round(1)
updated_df['BOD removal'] = updated_df['BOD removal'].fillna(updated_df['BOD removal'].median()).round(1)
updated_df['TSS F/mg/L'] = updated_df['TSS F/mg/L'].fillna(updated_df['TSS F/mg/L'].median()).round(1)
updated_df['TSS Eff/mg/L'] = updated_df['TSS Eff/mg/L'].fillna(updated_df['TSS Eff/mg/L'].median()).round(1)
updated_df['TSS removal'] = updated_df['TSS removal'].fillna(updated_df['TSS removal'].median()).round(1)

# Getting dataset
X = updated_df[['pH Reactor', 'pH F', 'pH Eff', 'COD F/mg/L', 'COD Eff/mg/L', 'COD removal', 'BOD F/mg/L', 'BOD Eff/mg/L', 'BOD removal']].values
y = updated_df[['CH4', 'CO2', 'H2S']].values

x = []
x = np.concatenate((x, ['pH Reactor']))
x = np.concatenate((x, ['pH F']))
x = np.concatenate((x, ['pH Eff']))
x = np.concatenate((x, ['COD F/mg/L']))
x = np.concatenate((x, ['COD Eff/mg/L']))
x = np.concatenate((x, ['COD removal']))
x = np.concatenate((x, ['BOD F/mg/L']))
x = np.concatenate((x, ['BOD Eff/mg/L']))
x = np.concatenate((x, ['BOD removal']))
xData = updated_df[x].values


#Standardized and Normalized the dataset
#sc_X = StandardScaler()
#sc_y = StandardScaler()

#X = sc_X.fit_transform(X)
#y = sc_y.fit_transform(y)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(xData, y, test_size=0.20, random_state=0)

# Create the Linear Regression SVR regressor
lr = LinearRegression()
svr = SVR(kernel='rbf')
neural_network = MLPRegressor(random_state=0, max_iter=500)

# Create the Multioutput Regressor
multiOutputLR = MultiOutputRegressor(lr)
multiOutputSVR = MultiOutputRegressor(svr)
multiOutputANN = MultiOutputRegressor(neural_network)

# Train the regressor
multiOutputLR = multiOutputLR.fit(X_train, y_train)
multiOutputSVR = multiOutputSVR.fit(X_train, y_train)
multiOutputANN = multiOutputANN.fit(X_train, y_train)

# Generate predictions for testing data
y_pred_LR = multiOutputLR.predict(X_test)
y_pred_SVR = multiOutputSVR.predict(X_test)
y_pred_ANN = multiOutputANN.predict(X_test)

print(y_pred_SVR)

score_LR = multiOutputLR.score(X_test,y_test)
score_SVR = multiOutputSVR.score(X_test,y_test)
score_ANN = multiOutputANN.score(X_test,y_test)
print(f'Score for LR: {score_LR} - Score for SVR: {score_SVR} - Score for ANN: {score_ANN}')

# Evaluate the regressor
mse_one_LR = mean_squared_error(y_test[:,0], y_pred_LR[:,0])
mse_two_LR = mean_squared_error(y_test[:,1], y_pred_LR[:,1])
mse_three_LR = mean_squared_error(y_test[:,2], y_pred_LR[:,2])
print(f'MSE: CH4 for LR: {mse_one_LR} - CO2 for LR: {mse_two_LR} - H2S for LR: {mse_three_LR}')
mae_one_LR = mean_absolute_error(y_test[:,0], y_pred_LR[:,0])
mae_two_LR = mean_absolute_error(y_test[:,1], y_pred_LR[:,1])
mae_three_LR = mean_absolute_error(y_test[:,2], y_pred_LR[:,2])
print(f'MAE: CH4 for LR: {mae_one_LR} - CO2 for LR: {mae_two_LR}  H2S for LR: {mae_three_LR}')

mse_one_SVR = mean_squared_error(y_test[:,0], y_pred_SVR[:,0])
mse_two_SVR = mean_squared_error(y_test[:,1], y_pred_SVR[:,1])
mse_three_SVR = mean_squared_error(y_test[:,2], y_pred_SVR[:,2])
print(f'MSE: CH4 for SVR: {mse_one_SVR} - CO2 for SVR: {mse_two_SVR} - H2S for SVR: {mse_three_SVR}')
mae_one_SVR = mean_absolute_error(y_test[:,0], y_pred_SVR[:,0])
mae_two_SVR = mean_absolute_error(y_test[:,1], y_pred_SVR[:,1])
mae_three_SVR = mean_absolute_error(y_test[:,2], y_pred_SVR[:,2])
print(f'MAE: CH4 for SVR: {mae_one_SVR} - CO2 for SVR: {mae_two_SVR}  H2S for SVR: {mae_three_SVR}')

mse_one_ANN = mean_squared_error(y_test[:,0], y_pred_ANN[:,0])
mse_two_ANN = mean_squared_error(y_test[:,1], y_pred_ANN[:,1])
mse_three_ANN = mean_squared_error(y_test[:,2], y_pred_ANN[:,2])
print(f'MSE: CH4 for ANN: {mse_one_ANN} - CO2 for ANN: {mse_two_ANN} - H2S for ANN: {mse_three_ANN}')
mae_one_ANN = mean_absolute_error(y_test[:,0], y_pred_ANN[:,0])
mae_two_ANN = mean_absolute_error(y_test[:,1], y_pred_ANN[:,1])
mae_three_ANN = mean_absolute_error(y_test[:,2], y_pred_ANN[:,2])
print(f'MAE: CH4 for ANN: {mae_one_ANN} - CO2 for ANN: {mae_two_ANN}  H2S for ANN: {mae_three_ANN}')
