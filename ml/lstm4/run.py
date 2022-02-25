import app
from ml.lstm4.VXXDataset import VXXDataset
from ml.lstm4.model import get_lstm4_model
from ml.plugins.tensorboard_callback import get_tensor_board_callback, named_logs

if __name__ == '__main__':
    model = get_lstm4_model()

    ds = VXXDataset(batch_size=1, testing_batch_size=1)
    x, y = ds.get_data_set()
    test_x, test_y = ds.get_test_data_set()
    print("get all the data")
    logs = model.train_on_batch(x, y)

    logs2 = model.test_on_batch(test_x, test_y)

    tensorboard = get_tensor_board_callback("lstm4", 3)
    tensorboard.set_model(model)

    tensorboard.on_train_batch_end(1, named_logs(model, logs))
    tensorboard.on_test_batch_end(1, named_logs(model, logs2))
