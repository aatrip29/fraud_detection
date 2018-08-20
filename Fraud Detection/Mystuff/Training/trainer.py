from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
from sklearn import metrics
import pandas as pd
import os


class train:

    def trainer(df, replace_model=False):

        # if isinstance(df, pd.DataFrame):
        #     raise ValueError("Invalid DataFrame")

        # array = df.values
        #
        # X = [list(map(float, val)) for val in array[:, :-1]]
        # y = [float(val) for val in array[:, -1]]

        # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state=7, shuffle=True)

        train, test = train_test_split(df, test_size=.3, random_state=7, shuffle=True)



        model_ada = None
        model_knn = None
        model_svr = None

        if ((not os.path.isfile("models/model_ada.pkl")) or replace_model) or (os.path.isfile("models/model_ada.pkl")):
            model_ada = AdaBoostRegressor(DecisionTreeRegressor(max_depth=5), n_estimators=200, random_state=13)
        else:
            model_ada = joblib.load("models/model_ada.pkl")

        if ((not os.path.isfile("models/model_svr.pkl")) or replace_model) or (os.path.isfile("models/model_svr.pkl")):
            model_svr = SVR(C=50,max_iter=3)
        else:
            model_svr = joblib.load("models/model_ada.pkl")

        if ((not os.path.isfile("models/model_knn.pkl")) or replace_model) or (os.path.isfile("models/model_knn.pkl")):
            model_knn = KNeighborsRegressor(n_neighbors=1)
        else:
            model_knn = joblib.load("models/model_knn.pkl")

        array = train.values
        X_train = array[:, :-1]
        y_train = array[:, -1]
        model_ada.fit(X_train, y_train)
        model_svr.fit(X_train, y_train)
        model_knn.fit(X_train, y_train)

        joblib.dump(model_ada, "models/model_ada.pkl")
        joblib.dump(model_svr, "models/model_svr.pkl")
        joblib.dump(model_knn, "models/model_knn.pkl")

        # print(test)
        array = train.values

        X_test = array[:, :-1]
        y_test = array[:, -1]

        y_pred_ada = model_ada.predict(X_test)
        y_pred_svr = model_svr.predict(X_test)
        y_pred_knn = model_knn.predict(X_test)

        # print(metrics.classification_report(y_test, y_pred_svr > 0.5))
        # print(metrics.classification_report(y_test, y_pred_knn > 0.5))
        # print(metrics.classification_report(y_test, y_pred_ada > 0.5))

        for c in range(0, len(y_test)):
            print(((y_pred_svr[c] + y_pred_knn[c] + y_pred_ada[c]) / 3), y_test[c])
