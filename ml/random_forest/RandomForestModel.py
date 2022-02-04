from sklearn.linear_model import SGDRegressor


class RandomForestModel(SGDRegressor):

    def __init__(self, name='randomForest', predict_day=3, score=None, *args, **kwargs):
        super(RandomForestModel, self).__init__(*args, **kwargs)
        self.name = name
        self.predict_day = predict_day
        self.score = score
