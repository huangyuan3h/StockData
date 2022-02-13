from flask import Flask


def register_router(app: Flask):
    from api.tasks import get_task
    from api.stock import sync_stocks
    from api.kline import get_stock_data, sync_stock_by_code, sync_all_stock
    from api.index_kline import sync_index_kline_by_code
    from api.lstm import training_lstm, predict_n_day_by_stock_code, generate_n_day_report
    from api.fund_flow import sync_all_fund_flow, sync_fund_flow_by_code

    app.add_url_rule('/tasks', 'tasks', methods=['get'], view_func=get_task)
    # functional endpoint
    app.add_url_rule('/sync/stocks', 'sync_stocks', methods=['get'], view_func=sync_stocks)

    app.add_url_rule('/sync/kline/all', 'sync_all_stock', methods=['get'], view_func=sync_all_stock)

    app.add_url_rule('/sync/kline_by_code/<string:code>', 'sync_kline_by_code', methods=['get'],
                     view_func=sync_stock_by_code)

    app.add_url_rule('/sync/index_kline_by_code/<string:code>', 'sync_index_kline_by_code', methods=['get'],
                     view_func=sync_index_kline_by_code)

    app.add_url_rule('/sync/fund_flow/all', 'sync_fund_flow_all', methods=['get'],
                     view_func=sync_all_fund_flow)

    app.add_url_rule('/sync/fund_flow_by_code/<string:code>', 'sync_fund_flow_by_code', methods=['get'],
                     view_func=sync_fund_flow_by_code)

    app.add_url_rule('/stock/<string:code>', 'get_stock_data', methods=['get'], view_func=get_stock_data)

    app.add_url_rule('/training/<string:model>/<int:predict_day>/<int:num>', 'training_lstm', methods=['get'],
                     view_func=training_lstm)

    app.add_url_rule('/predict/<string:model>/<int:predict_day>/<string:code>', 'predict_lstm_by_code', methods=['get'],
                     view_func=predict_n_day_by_stock_code)

    app.add_url_rule('/report/<string:model>/<int:predict_day>', 'generate_decision_tree_report', methods=['get'],
                     view_func=generate_n_day_report)
