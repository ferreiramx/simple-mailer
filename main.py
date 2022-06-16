import config
from mail_utils import send_email
from gspread_pandas import Spread

# Read the Google Sheets document
spread = Spread(config.GSHEETS_DOCUMENT, sheet = config.GSHEETS_SHEET)

# Convert spreadsheet to DataFrame
data = spread.sheet_to_df(index = None)

# Send emails
data.apply(lambda row: send_email(row), axis = 1)