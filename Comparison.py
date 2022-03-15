# Data Manipulation
import pandas as pd # for data manipulation

# Sklearn
from sklearn.svm import SVR # for building SVR model
from sklearn.linear_model import LinearRegression # for building Linear Regression model
from sklearn.multioutput import MultiOutputRegressor # To make the output be independent to each other
from sklearn.model_selection import train_test_split # Split the training and testing data to do comparison
from sklearn.metrics import mean_squared_error, mean_absolute_error # To do comparison
from sklearn.preprocessing import StandardScaler # Standardized and normalized the x and y data

dataset = pd.read_excel('Data_SEGP.xlsx')
dataset.drop("Unnamed: 18", axis=1, inplace=True)
dataset.drop("Unnamed: 19", axis=1, inplace=True)
dataset.drop("Unnamed: 20", axis=1, inplace=True)
dataset.drop("Unnamed: 21", axis=1, inplace=True)
print(dataset.isnull().sum())

updated_df = dataset
updated_df['CH4'] = updated_df['CH4'].fillna(updated_df['CH4'].mean()).round(1)
updated_df['Volume Biogas/L'] = updated_df['Volume Biogas/L'].fillna(updated_df['Volume Biogas/L'].mean()).round(1)
updated_df['H2S'] = updated_df['H2S'].fillna(updated_df['H2S'].mean()).round(1)
updated_df['CO2'] = updated_df['CO2'].fillna(updated_df['CO2'].mean()).round(1)
updated_df['pH Reactor'] = updated_df['pH Reactor'].fillna(updated_df['pH Reactor'].mean()).round(1)
updated_df['pH F'] = updated_df['pH F'].fillna(updated_df['pH F'].mean()).round(1)
updated_df['pH Eff'] = updated_df['pH Eff'].fillna(updated_df['pH Eff'].mean()).round(1)
updated_df['ORL gCOD/Ld'] = updated_df['ORL gCOD/Ld'].fillna(updated_df['ORL gCOD/Ld'].mean()).round(1)
updated_df['COD F/mg/L'] = updated_df['COD F/mg/L'].fillna(updated_df['COD F/mg/L'].mean()).round(1)
updated_df['COD Eff/mg/L'] = updated_df['COD Eff/mg/L'].fillna(updated_df['COD Eff/mg/L'].mean()).round(1)
updated_df['COD removal'] = updated_df['COD removal'].fillna(updated_df['COD removal'].mean()).round(1)
updated_df['BOD F/mg/L'] = updated_df['BOD F/mg/L'].fillna(updated_df['BOD F/mg/L'].mean()).round(1)
updated_df['BOD Eff/mg/L'] = updated_df['BOD Eff/mg/L'].fillna(updated_df['BOD Eff/mg/L'].mean()).round(1)
updated_df['BOD removal'] = updated_df['BOD removal'].fillna(updated_df['BOD removal'].mean()).round(1)
updated_df['TSS F/mg/L'] = updated_df['TSS F/mg/L'].fillna(updated_df['TSS F/mg/L'].mean()).round(1)
updated_df['TSS Eff/mg/L'] = updated_df['TSS Eff/mg/L'].fillna(updated_df['TSS Eff/mg/L'].mean()).round(1)
updated_df['TSS removal'] = updated_df['TSS removal'].fillna(updated_df['TSS removal'].mean()).round(1)

# Getting dataset
X = dataset[['pH Reactor', 'pH F', 'pH Eff', 'COD F/mg/L', 'COD Eff/mg/L', 'COD removal', 'BOD F/mg/L', 'BOD Eff/mg/L', 'BOD removal']].values
y = dataset[['CH4', 'CO2', 'H2S']].values


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