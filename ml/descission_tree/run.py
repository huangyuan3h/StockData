import app
from ml.data.prepare import get_stock_data_greater_then_min_size, get_stock_data_by_size, get_change_by_mask_size
from ml.descission_tree.model import decision_tree

if __name__ == '__main__':
    df = get_stock_data_greater_then_min_size(70, 500)
    df2 = get_stock_data_by_size(df, 70)
    percentage = get_change_by_mask_size(df2, 10, 0)
    decision_tree.fit(df2, percentage)
