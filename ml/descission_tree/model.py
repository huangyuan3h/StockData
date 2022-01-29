import joblib
from sklearn.tree import DecisionTreeRegressor

default_path = 'model_data/decision_tree.pkl'


class DecisionTreeModel(object):
    loaded = False

    def __init__(self, path=default_path):
        self.decision_tree = DecisionTreeRegressor()
        self.path = path

    def load_model(self, path=None):
        loading_path = path if path is not None else self.path
        self.loaded = True
        self.decision_tree = joblib.load(loading_path)

    def save_model(self):
        joblib.dump(self.decision_tree, self.path)

    def fit(self, X, y):
        self.decision_tree.fit(X, y)

    def predict(self, X):
        return self.decision_tree.predict(X)


decision_tree = DecisionTreeModel()
