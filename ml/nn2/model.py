from tensorflow.keras import layers, callbacks, Sequential


def get_nn_model(shape_size=840, hidden_layer_size=1024):
    model = Sequential([
        layers.Dense(hidden_layer_size, activation='relu', input_shape=[shape_size]),
        layers.Dense(hidden_layer_size, activation='relu'),
        layers.Dense(hidden_layer_size, activation='relu'),
        layers.Dense(1),
    ])
    model.compile(
        optimizer='adam',
        loss='mae',
    )
    return model


def get_early_stop_callback():
    early_stopping = callbacks.EarlyStopping(
        min_delta=0.001,  # minimium amount of change to count as an improvement
        patience=20,  # how many epochs to wait before stopping
        restore_best_weights=True,
    )
    return early_stopping
