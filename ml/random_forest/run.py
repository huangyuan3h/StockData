import app
from sklearn.metrics import mean_absolute_error

from ml.random_forest.RandomForestModelFactory import RandomForestModelFactory

if __name__ == '__main__':
    batch_size = 100
    factory = RandomForestModelFactory(predict_day=3, path='../../model_data/randomForest_3.pkl')
    ds = factory.data_set
    model = factory.model


    X, y = ds.get_data_set()
    model.fit(X, y)
    # verify
    testing_X, testing_y = ds.get_test_data_set()
    predict_y = model.predict(testing_X)
    score = mean_absolute_error(testing_y, predict_y)

    print(score)
