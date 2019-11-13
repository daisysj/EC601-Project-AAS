import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor


data = pd.read_csv("/Users/liuyu/Downloads/Admission_Predict_ver1.1.csv", sep = ",")
scalar = preprocessing.MinMaxScaler()
scalar_fit = scalar.fit(data[['GRE Score', 'TOEFL Score']])
normalized_score = scalar_fit.transform(data[['GRE Score', 'TOEFL Score']])

data2 = pd.read_csv("/Users/liuyu/Downloads/Admission_Predict.csv", sep = ",")
scalar2 = preprocessing.MinMaxScaler()
scalar_fit2 = scalar2.fit(data2[['GRE Score', 'TOEFL Score']])
normalized_score2 = scalar_fit2.transform(data2[['GRE Score', 'TOEFL Score']])


normalized_data = pd.DataFrame(normalized_score, columns = ['GRE Score', 'TOEFL Score'])
data['GRE Score'] = normalized_data['GRE Score']
data['TOEFL Score'] = normalized_data['TOEFL Score']

normalized_data2 = pd.DataFrame(normalized_score2, columns = ['GRE Score', 'TOEFL Score'])
data2['GRE Score'] = normalized_data2['GRE Score']
data2['TOEFL Score'] = normalized_data2['TOEFL Score']

predictor = list(data.columns)
predictor.remove('Serial No.')
predictor.remove('Chance of Admit ')

predictor2 = list(data2.columns)
predictor2.remove('Serial No.')
predictor2.remove('Chance of Admit ')

X_train = data[predictor].values
y_train = data['Chance of Admit '].values
X_test = data2[predictor2].values
y_test = data2['Chance of Admit '].values


classifier = RandomForestRegressor(n_estimators=200, criterion='mse')
RF = classifier.fit(X_train, y_train)
PredAdmit = RF.predict(X_test)

# Creating a DataFrame of Testing data
AdmitData = pd.DataFrame(X_test, columns = predictor)
AdmitData['ChancesOfAdmit'] = y_test
AdmitData['PredictedChancesOfAdmit'] = PredAdmit
AdmitData.head()
print(AdmitData.head())


AdmitData['error']=100 * (abs(AdmitData['ChancesOfAdmit'] - AdmitData['PredictedChancesOfAdmit'])/AdmitData['ChancesOfAdmit'])
print('Mean Absolute Percent Error: ',round(np.mean(AdmitData['error'])), '%')
print('Average Accuracy of the model: ',100 - round(np.mean(AdmitData['error'])), '%')
