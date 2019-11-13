import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
import seaborn as sns
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Lasso,Ridge,BayesianRidge,LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import warnings


def visualisation():

    #GRE
    fig = sns.distplot(data['GRE Score'], kde=False)
    plot.title("Distribution of GRE Scores")
    plot.show()
    #TOEFL
    fig = sns.distplot(data['TOEFL Score'], kde=False)
    plot.title("Distribution of TOEFL Scores")
    plot.show()
    plot.scatter(data["University Rating"],data.CGPA)
    plot.title("CGPA Scores vs University Ratings")
    plot.xlabel("University Rating")
    plot.ylabel("CGPA")
    plot.show()
    #Research
    y = np.array([len(data[data.Research == 0]),len(data[data.Research == 1])])
    x = ["Not Having Research","Having Research"]
    plot.bar(x,y)
    plot.title("Research Experience")
    plot.xlabel("Canditates")
    plot.ylabel("Frequency")
    plot.show()


def models():

    models = [['DecisionTree :', DecisionTreeRegressor()],
              ['Linear Regression :', LinearRegression()],
              ['Random Forest :', RandomForestRegressor()],
              ['Lasso: ', Lasso()],
              ['Ridge: ', Ridge()],
              ['Bayesian Ridge: ', BayesianRidge()]]

    for name, model in models:
        model.fit(X_train, y_train)
        predict = model.predict(X_test)
        print(name, (np.sqrt(mean_squared_error(y_test, predict))))


def feature_importances():

    classifier = RandomForestRegressor()
    classifier.fit(X, y)
    importance = pd.DataFrame()
    importance['Features'] = X.columns
    importance['Importance'] = classifier.feature_importances_
    importance = importance.sort_values(by=['Importance'], ascending=False)
    print(importance)


if __name__ == "__main__":

    #Initialization
    warnings.filterwarnings("ignore")
    data = pd.read_csv("/Users/liuyu/Downloads/Admission_Predict_ver1.1.csv", sep=",")
    print(data.info())
    print(data.head())
    X = data.drop(['Chance of Admit '], axis=1)
    X = X.drop(['Serial No.'], axis=1)
    y = data['Chance of Admit ']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, shuffle=False)
    #visualisation()
    models()
    feature_importances()
