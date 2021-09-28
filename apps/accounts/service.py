

import pandas as pd
import dateparser

from apps.utils.cache import timed_cache
from apps.utils.google_sheets import open_workbook

def replace_empty_str(sname: str):
    if sname == "":
        return "Product"
    return sname.lower().capitalize()

@timed_cache(60*15)
def process_daily_salesworkbook_data(workbook_name):

# open workbook
    workbook = open_workbook(workbook_name)
    worksheet_list = workbook.worksheets()
    
    # process raw worksheet data
    dates = [worksheet.acell('B2').value for worksheet in worksheet_list]

    # append 
    dataframes = []
    for idx,worksheet in enumerate(worksheet_list):
        df = pd.DataFrame(worksheet.get_all_records(head=3), columns=["","OPEN","ADD","SOLD","CLOSE", "TOTAL"])
        
        # replace empty vals
        df.fillna(0, inplace=True)
        
        # reame columns
        df.rename(columns={"":"Product", "OPEN":"Open", "ADD":"Add","SOLD":"Sold","CLOSE":"Close", "TOTAL":"Total"}, inplace=True)

        # add date column
        date_col = [dates[idx] for i in list(range(len(df)))]
        df["Date"] = date_col

        dataframes.append(df)
    
    return dataframes
    