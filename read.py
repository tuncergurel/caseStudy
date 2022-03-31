from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google.oauth2 import service_account
from main import main as crt

# If modifying these scopes, delete the file token.json.

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'sheet_test.json'

credentials = None
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID = '1Z5lUkXkocle-uVwQCVVg42dIG81GXVbPg3Qn-ZZ2o10'


service = build('sheets', 'v4', credentials=credentials)

sheet = service.spreadsheets()

service.spreadsheets().values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sayfa1!A1:Z1089").execute()

listoflist = [["URL","NAME","PRICE","IN STOCK","OUT OF STOCK","CODE"]]
request = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sayfa1!A1:X1",valueInputOption="USER_ENTERED",
                                insertDataOption="OVERWRITE", body= {"values":listoflist}).execute()


def write():
        datas = crt()

        liste = []
        for i in datas:
                liste.append(i)

        sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sayfa1!A1:X1",
                                   valueInputOption="USER_ENTERED", insertDataOption="INSERT_ROWS", body={"values": liste}).execute()

        print("Completed")
write()
