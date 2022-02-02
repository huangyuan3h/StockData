from pandas import DataFrame

from ml.data.prepare import choose_a_random_stock_code, get_stock_data, get_stock_data_greater_then_min_size, \
    get_stock_data_by_size, get_change_by_mask_size


def test_choose_a_random_stock_code(mocker):
    fn = mocker.patch('dao.stock_process.get_stock_code_list')
    fn.return_value = ['mock']
    result = choose_a_random_stock_code()
    fn.assert_called_once_with()
    assert result is 'mock'


def test_get_stock_data(mocker):
    mock_get_kline_by_code = mocker.patch('dao.kline_process.get_kline_by_code')
    mock_choose_code = mocker.patch('ml.data.prepare.choose_a_random_stock_code')
    mock_kline_2_dataframe = mocker.patch('dao.mapping.kline_mapping.kline_obj_2_dataframe')
    mock_choose_code.return_value = 'mock_code'
    get_stock_data()

    mock_get_kline_by_code.assert_called_with('mock_code', 500)
    mock_kline_2_dataframe.assert_called()


def test_get_stock_data_greater_then_min_size(mocker):
    mock_get_stock_data = mocker.patch('ml.data.prepare.get_stock_data')
    mock_get_stock_data.return_value = DataFrame([{1, 2, }, {2, 3}])
    result = get_stock_data_greater_then_min_size(1)
    assert result is mock_get_stock_data.return_value


def test_get_stock_data_by_size():
    mock_df = DataFrame([{1, 2, }, {2, 3}])
    result = get_stock_data_by_size(mock_df, 1, 1)
    assert len(result.compare(DataFrame([{2, 3}]))) == 0


def test_get_change_by_mask_size():
    mock_df = DataFrame([{1, 2}, {2, 3}], columns=["close", "open"])
    result = get_change_by_mask_size(mock_df, 1)

    assert result == -50.0
