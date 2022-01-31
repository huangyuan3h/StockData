import joblib
from sklearn.ensemble import RandomForestRegressor

file_format = 'model_data/%(filename)-%(predictDay)-%(timestamp)-%(score).pkl'


class DecisionTreeModel(object):
    loaded = False

    def __init__(self, filename='randomForest', predict_day=3, path=None):
        self.random_forest = RandomForestRegressor()
        self.filename = filename
        self.predict_day = predict_day
        self.path = path

    def load_model(self, path=None):
        loading_path = path if path is not None else self.path
        self.loaded = True
        self.random_forest = joblib.load(loading_path)

    def save_model(self):
        joblib.dump(self.random_forest, self.path)

    def fit(self, X, y):
        self.random_forest.fit(X, y)

    def predict(self, X):
        return self.random_forest.predict(X)
