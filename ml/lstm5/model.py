from tensorflow.keras import layers, Sequential, optimizers, losses, metrics



def get_lstm5_model(n_steps=60, n_features=23, lstm_layer_size=2048):
    model = Sequential([
        layers.LSTM(units=lstm_layer_size, return_sequences=True, input_shape=(n_steps, n_features), name="lstm1"),
        layers.LSTM(int(lstm_layer_size / 2 ** 1), return_sequences=False, name="lstm2"),
        layers.BatchNormalization(),
        layers.Dropout(0.1),
        layers.Dense(int(lstm_layer_size / 2 ** 2), activation='relu', name="dense1"),
        layers.Dense(int(lstm_layer_size / 2 ** 3), activation='relu', name="dense2"),
        layers.Dense(1),
    ])
    # 简单来说，MSE计算简便，但MAE对异常点有更好的鲁棒性
    model.compile(
        optimizer='sgd',
        loss='mae',
        metrics=['mae'],
    )
    return model
