from sklearn.metrics import mean_absolute_error

from log import log
from ml.random_forest.RandomForestModelFactory import RandomForestModelFactory
from task_manager import task_manager


@task_manager.celery.task()
def training_random_forest(predict_day=3, batch_size=10):
    factory = RandomForestModelFactory(predict_day=predict_day)
    ds = factory.data_set
    model = factory.model
    testing_X, testing_y = ds.get_test_data_set()
    for i in range(batch_size):
        try:
            X, y = ds.get_data_set()
            model.partial_fit(X, y)
            # verify
            predict_y = model.predict(testing_X)
            score = mean_absolute_error(testing_y, predict_y)
            log.info(f'training random forest 3: No. {i} with score: {score}')
            # save to file
            result = factory.save(score, verify=False)
            if not result:
                log.info(f'training save failed, current score: {model.score}, training_score:{score}')
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
