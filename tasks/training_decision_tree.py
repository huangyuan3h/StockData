from log import log
from ml.data.BaseDataset import BaseDataset
from ml.descission_tree.model import decision_tree
from ml.descission_tree.verify import verify_by_mean_absolute_error
from task_manager import task_manager


@task_manager.celery.task()
def training_decision_tree(batch_size=10):

    if not decision_tree.loaded:
        decision_tree.load_model()

    for i in range(batch_size):
        ds = BaseDataset(60, 10, 1000)
        X, y = ds.get_data_set()
        decision_tree.fit(X, y)
        log.info("training decision tree: No. %s  finished", i)

    decision_tree.save_model()
    log.info("training decision tree %s times", batch_size)
    result = verify_by_mean_absolute_error(decision_tree)
    log.info("mean absolute error for current model is ", result)


