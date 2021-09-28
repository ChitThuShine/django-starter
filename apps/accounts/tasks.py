from datetime import datetime
import os
import pathlib
import dateparser
from apps.accounts.service import process_daily_salesworkbook_data
from deta import Deta
from tinydb import TinyDB, Query

from huey import crontab
from huey.contrib.djhuey import db_periodic_task, db_task



BASE_PATH = pathlib.Path(__file__).parent.parent.resolve()

deta = Deta("a0udcn2d_Y85y2XiSSSLjTNPtGLV6YsFZZ6mSxBLu")
db = deta.Base("accounts")


logs_db = TinyDB(os.path.join(BASE_PATH, 'db/logs.json'))
sales_db = TinyDB(os.path.join(BASE_PATH, 'db/sales.json'))
costs_db = TinyDB(os.path.join(BASE_PATH, 'db/costs.json'))

Sales = Query()
Costs = Query()
Logs = Query()


@db_periodic_task(crontab(minute='*/5'))
def sync_daily_sales_file_to_db(force_update = False):

    # check last sync is before today
    should_update = True
    
    last_sync_str = logs_db.search(Logs.id == "sales_last_sync")
    print(last_sync_str, "fetch result")
    if len(last_sync_str) > 0:
        last_sync_date = dateparser.parse(last_sync_str[0]['date'])
        should_update = datetime.now().date() != last_sync_date.date()

    if force_update:
        should_update = True

    print(f"Should update? {should_update}")
    if should_update:
        records = []
        dataframes = process_daily_salesworkbook_data('demo')
        for dataframe in dataframes:
            records.extend(dataframe.to_dict(orient="records"))

        print("write to db")
        sales_db.insert_multiple(records)
        date_sync = datetime.now().strftime("%Y-%m-%d")
        logs_db.upsert({"id":"sales_last_sync", "date":date_sync }, Logs.id=='sales_last_sync')

    return None



def fetch_daily_sales():
    records = sales_db.all()
    for record in records:
        for k,v in record.items():
            if k in ["Add","Open","Close","Sold","Total"] and v == '':
                record[k]=0


        record["Date"] = dateparser.parse(record["Date"])

    return records
