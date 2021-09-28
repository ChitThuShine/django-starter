import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pathlib


# use creds to create a client to interact with the Google Drive API
scope = ['https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive']

path = pathlib.Path(__file__).parent.parent.resolve()
creds = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(path, 'credentials.json'), scope)
client = gspread.authorize(creds)

def open_workbook(workbook_name):
    """Returns open workbook or None"""
    return client.open(workbook_name)
