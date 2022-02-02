import app
from ml.random_forest.RandomForestModelFactory import RandomForestModelFactory

if __name__ == '__main__':
    batch_size = 100
    factory = RandomForestModelFactory(predict_day=3, path='../../model_data/randomForest_3.pkl')
    ds = factory.data_set
    model = factory.model

    X, y = ds.get_data_set()
    model.fit(X, y)



    "verify"

