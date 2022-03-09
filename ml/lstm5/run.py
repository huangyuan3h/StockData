import app
import keras
import keras.backend as K
from ml.lstm4.VXXDataset import VXXDataset
from ml.lstm5.model import get_lstm5_model

if __name__ == '__main__':
    model = keras.models.load_model('model_data/lstm5_3')
    # print(model.layers[0].weights[0][0][0])
    # ds = VXXDataset(chart_size=60, mask_size=3, batch_size=100)
    # X, y = ds.get_data_set()
    # learning_rate = K.eval(model.optimizer.lr)
    # print(learning_rate)
    # history = model.train_on_batch(X, y)
    # print(history)
    # history = model.train_on_batch(X, y)
    # print(history)
    # print(model.layers[0].weights[0][0][0])
    ds = VXXDataset(chart_size=60, mask_size=3, batch_size=100)
    X, y = ds.get_data_set()
    print(model.layers[0].weights[0][0][0])
    model.fit(X, y, validation_split=0.3, epochs=1)
    print(model.layers[0].weights[0][0][0])
    model.save('model_data/lstm5_3')

   # K.set_value(model.optimizer.learning_rate, current_learning_rate)


