from ml.data.prepare import choose_a_random_stock_code


def test_choose_a_random_stock_code(mocker):
    fn = mocker.patch('dao.stock_process.get_stock_code_list')
    fn.return_value = ['mock']
    result = choose_a_random_stock_code()
    fn.assert_called_once_with()
    assert result is 'mock'

