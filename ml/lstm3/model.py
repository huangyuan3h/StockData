from tensorflow.keras import layers, Sequential


def get_lstm3_model(n_steps=60, n_features=20, lstm_layer_size=2048):
    model = Sequential([
        layers.LSTM(units=lstm_layer_size, return_sequences=True, input_shape=(n_steps, n_features)),
        layers.LSTM(int(lstm_layer_size / 2 ** 1), return_sequences=True),
        layers.LSTM(int(lstm_layer_size / 2 ** 2), return_sequences=True),
        layers.LSTM(int(lstm_layer_size / 2 ** 3), return_sequences=False),
        layers.BatchNormalization(),
        layers.Dropout(0.1),
        layers.Dense(int(lstm_layer_size / 2 ** 4), activation='elu'),
        layers.BatchNormalization(),
        layers.Dropout(0.1),
        layers.Dense(int(lstm_layer_size / 2 ** 5), activation='elu'),
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
