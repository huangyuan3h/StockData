from tensorflow.keras import layers, callbacks, Sequential


def get_lstm_model(n_steps=60, n_features=14, lstm_layer_size=2048):
    model = Sequential([
        layers.LSTM(units=lstm_layer_size, input_shape=(n_steps, n_features)),
        layers.Dense(1),
    ])
    model.compile(
        optimizer='sgd',
        loss='mae',
        metrics=['mae'],
    )
    return model


def get_early_stop_callback():
    early_stopping = callbacks.EarlyStopping(
        min_delta=0.001,  # minimium amount of change to count as an improvement
        patience=20,  # how many epochs to wait before stopping
        restore_best_weights=True,
    )
    return early_stopping