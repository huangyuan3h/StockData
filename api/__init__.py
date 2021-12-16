from flask import Flask

from api.GetTasks import get_task
from api.KLineDayDataByStockCode import start_sync_stock_by_code
from api.KlineAllStock import sync_all_stock
from api.StockList import start_sync_stock_list


def register_router(app: Flask):
    app.add_url_rule('/tasks', 'tasks', methods=['get'], view_func=get_task)

    # functional endpoint
    app.add_url_rule('/sync/StockList', 'sync_stock_lists', methods=['get'], view_func=start_sync_stock_list)
    app.add_url_rule('/sync/KLineDay/<string:code>', 'sync_stock_by_day', methods=['get'],
                     view_func=start_sync_stock_by_code)
    app.add_url_rule('/sync/KLineAllDay', 'sync_all_stock', methods=['get'], view_func=sync_all_stock)
