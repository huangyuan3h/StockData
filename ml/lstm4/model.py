from tensorflow.keras import layers, Sequential


def get_lstm4_model(n_steps=60, n_features=23, lstm_layer_size=2048):
    model = Sequential([
        layers.LSTM(units=lstm_layer_size, return_sequences=True, input_shape=(n_steps, n_features), name="lstm1"),
        layers.LSTM(int(lstm_layer_size / 2 ** 1), return_sequences=True, name="lstm2"),
        layers.LSTM(int(lstm_layer_size / 2 ** 2), return_sequences=True, name="lstm3"),
        layers.LSTM(int(lstm_layer_size / 2 ** 3), return_sequences=False, name="lstm4"),
        layers.BatchNormalization(),
        layers.Dropout(0.1),
        layers.Dense(int(lstm_layer_size / 2 ** 4), activation='elu', name="dense1"),
        layers.BatchNormalization(),
        layers.Dropout(0.1),
        layers.Dense(int(lstm_layer_size / 2 ** 5), activation='elu', name="dense2"),
        layers.BatchNormalization(),
        layers.Dropout(0.1),
        layers.Dense(1),
    ])
    model.compile(
        optimizer='sgd',
        loss='mae',
        metrics=['mae'],
    )
    return model
