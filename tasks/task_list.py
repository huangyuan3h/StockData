from tasks.SyncStockListTask import SyncStockListTask
import uuid

sync_stock_list_task = SyncStockListTask('sync stock list', task_id=uuid.UUID('36be2d5f-dbce-4924-a2ae-c5cbe8b8b0a0'))


task_list = [sync_stock_list_task]
