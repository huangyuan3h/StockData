from tensorflow.keras import layers, Sequential, optimizers, losses, metrics



def get_lstm5_model(n_steps=60, n_features=23, lstm_layer_size=2048):
    model = Sequential([
        layers.LSTM(units=lstm_layer_size, return_sequences=True, input_shape=(n_steps, n_features)),
        layers.Dropout(0.2),
        layers.LSTM(int(lstm_layer_size / 2 ** 1), return_sequences=True),
        layers.Dropout(0.1),
        layers.LSTM(int(lstm_layer_size / 2 ** 2), return_sequences=True),
        layers.LSTM(int(lstm_layer_size / 2 ** 3), return_sequences=True),
        layers.LSTM(int(lstm_layer_size / 2 ** 4), return_sequences=True),
        layers.LSTM(int(lstm_layer_size / 2 ** 5), return_sequences=False),
        layers.Dense(int(lstm_layer_size / 2 ** 6), activation='elu'),
        layers.Dense(1),
    ])
    # 简单来说，MSE计算简便，但MAE对异常点有更好的鲁棒性
    model.compile(
        optimizer='adam',
        loss='mae',
        metrics=['mae'],
    )
    return model
