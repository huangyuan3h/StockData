from sklearn.metrics import mean_absolute_error

from log import log
from ml.random_forest.RandomForestModelFactory import RandomForestModelFactory
from task_manager import task_manager


@task_manager.celery.task()
def training_random_forest_3(batch_size=10):
    factory = RandomForestModelFactory(predict_day=3)
    ds = factory.data_set
    model = factory.model
    testing_X, testing_y = ds.get_test_data_set()
    for i in range(batch_size):
        X, y = ds.get_data_set()
        model.fit(X, y)
        # verify
        predict_y = model.predict(testing_X)
        score = mean_absolute_error(testing_y, predict_y)
        log.info(f'training random forest 3: No. {i} with score: {score}')
        # save to file
        result = factory.save(score)
        if not result:
            log.info(f'training save failed, current score: {model.score}, training_score:${score}')
            break
