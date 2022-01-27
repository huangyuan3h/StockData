import app
from ml.data.prepare import get_stock_data_greater_then_min_size, get_stock_data_by_size, get_change_by_mask_size, \
    normalize_stock_data

from ml.descission_tree.DescissionDataset import DecisionTreeDataset
from ml.descission_tree.model import decision_tree

if __name__ == '__main__':
    for i in range(10):
        ds = DecisionTreeDataset(60, 10, 1000)
        X, y = ds.get_data_set()
        decision_tree.fit(X, y)


    df = get_stock_data_greater_then_min_size(70, 500)
    df2 = get_stock_data_by_size(df, 70, 0)

    train_df = df2[10:]
    nd_data = normalize_stock_data(train_df).to_numpy()

    nx, ny = nd_data.shape
    reshaped_data = nd_data.reshape(1, nx * ny)

    predicted_y = decision_tree.predict(reshaped_data)

    print(predicted_y)
    percentage = get_change_by_mask_size(df2, 10, 0)
    print(percentage)

