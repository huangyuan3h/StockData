import joblib
from sklearn.tree import DecisionTreeRegressor


class DecisionTreeModel(object):
    loaded = False

    path = 'model_data/decision_tree.pkl'

    def __init__(self):
        self.decision_tree = DecisionTreeRegressor()

    def load_model(self):
        self.loaded = True
        self.decision_tree = joblib.load(self.path)

    def save_model(self):
        joblib.dump(self.decision_tree, self.path)

    def fit(self, X, y):
        self.decision_tree.fit(X, y)


decision_tree = DecisionTreeModel()
