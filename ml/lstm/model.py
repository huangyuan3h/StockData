from tensorflow.keras import layers, callbacks, Sequential


def get_lstm_model(n_steps=60, n_features=14, lstm_layer_size=1024):
    model = Sequential([
        layers.LSTM(units=lstm_layer_size, input_shape=(n_steps, n_features)),
        layers.Dense(1),
    ])
    model.compile(
        optimizer='sgd',
        loss='mean_squared_error',
        metrics=['mean_squared_error'],
    )
    return model


