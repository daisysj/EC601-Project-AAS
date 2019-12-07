import pandas as pd
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor


def predict():
    # get training data
    data = pd.read_csv("./Admission_Predict_ver1.1.csv", sep = ",")
    scalar = preprocessing.MinMaxScaler()
    scalar_fit = scalar.fit(data[['GRE Score', 'TOEFL Score']])
    normalized_score = scalar_fit.transform(data[['GRE Score', 'TOEFL Score']])

    # get student data
    data2 = pd.read_csv("./YOUR_FILE.csv", sep = ",")
    scalar2 = preprocessing.MinMaxScaler()
    scalar_fit2 = scalar2.fit(data2[['GRE Score', 'TOEFL Score']])
    normalized_score2 = scalar_fit2.transform(data2[['GRE Score', 'TOEFL Score']])

    # normalizing TOEFL & GRE score
    normalized_data = pd.DataFrame(normalized_score, columns = ['GRE Score', 'TOEFL Score'])
    data['GRE Score'] = normalized_data['GRE Score']
    data['TOEFL Score'] = normalized_data['TOEFL Score']
    normalized_data2 = pd.DataFrame(normalized_score2, columns = ['GRE Score', 'TOEFL Score'])
    data2['GRE Score'] = normalized_data2['GRE Score']
    data2['TOEFL Score'] = normalized_data2['TOEFL Score']

    # pre-process data
    predictor = list(data.columns)
    predictor.remove('Serial No.')
    predictor.remove('Chance of Admit ')
    predictor2 = list(data2.columns)

    X_train = data[predictor].values
    y_train = data['Chance of Admit '].values
    X_test = data2[predictor2].values

    # training model
    classifier = RandomForestRegressor(n_estimators=200, criterion='mse')
    RF = classifier.fit(X_train, y_train)
    PredAdmit = RF.predict(X_test)[0]

    return PredAdmit


if __name__ == "__main__":
    A = predict()
    print(A)
