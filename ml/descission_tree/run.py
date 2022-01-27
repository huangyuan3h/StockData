import app
from ml.data.prepare import get_stock_data_greater_then_min_size, get_stock_data_by_size, get_change_by_mask_size, \
    normalize_stock_data, get_stock_data

from ml.descission_tree.model import decision_tree

if __name__ == '__main__':
    if not decision_tree.loaded:
        decision_tree.load_model('../../model_data/decision_tree.pkl')

    code = 'SH600460'
    df = get_stock_data(code, size=70)

    train_df = df[10:]
    nd_data = normalize_stock_data(train_df).to_numpy()

    nx, ny = nd_data.shape
    reshaped_data = nd_data.reshape(1, nx * ny)

    predicted_y = decision_tree.predict(reshaped_data)

    print(predicted_y)
    percentage = get_change_by_mask_size(df, 10, 0)
    print(percentage)

