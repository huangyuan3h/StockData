import joblib
from sklearn.tree import DecisionTreeRegressor


class DecisionTreeModel(object):
    loaded = False

    path = 'model_data/decision_tree.pkl'

    def __init__(self):
        self.decision_tree = DecisionTreeRegressor()

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
