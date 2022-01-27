from ml.data.prepare import get_stock_data_greater_then_min_size, normalize_stock_data, get_stock_data


def get_last_N_stock_data(code:str, size = 60):
    df = get_stock_data(code, size)
    nd_data = normalize_stock_data(df).to_numpy()
    return nd_data
