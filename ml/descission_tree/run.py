import app
from ml.data.prepare import get_stock_data_greater_then_min_size, get_stock_data_by_size, get_change_by_mask_size, \
    normalize_stock_data
from ml.descission_tree.model import decision_tree

if __name__ == '__main__':
    df = get_stock_data_greater_then_min_size(70, 500)
    df2 = get_stock_data_by_size(df, 70)
    percentage = get_change_by_mask_size(df2, 10, 0)
    train_df = df2[10:]

    nd_data = normalize_stock_data(train_df).to_numpy()
    nx, ny = nd_data.shape
    one_d_data = nd_data.reshape(1, nx * ny)
    decision_tree.fit(one_d_data, [percentage])
