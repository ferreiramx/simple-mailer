# CONFIGURATION FILE. ALL VARIABLES GO HERE

# Wait time between each email (seconds)
WAIT_TIME = 2

# Email parameters. Format email using HTML
EMAIL_SUBJECT = "Your subject here"
EMAIL_BODY = """
    <p>Your Email Body Here</p>
    <p>The payload list goes below:</p>
    {codes}
    <p>Bye!</p>
"""

# Gmail credentials. You need to input an Application Password, not your regular account password
SENDER_EMAIL = "your@email"
SENDER_PASSWORD = "your_password"

# Name of the Google Sheets document and the specific sheet you want to use
# Remember: gspread_pandas expects you to save a service account file with access to this spreadsheet in its directory
# Refer to the gspread_pandas documentation for more help authenticating 
GSHEETS_DOCUMENT = "Your GSheets document name here"
GSHEETS_SHEET = "Your desired spreadsheet tab name here"

# Column headers for the columns representing the name, email and a list of the columns that contain codes
# Change them according to the structure of your document
NAME_COLUMN = "ExampleName"
EMAIL_COLUMN = "ExampleEmail"
PAYLOAD_COLUMNS = ["ExamplePayload 1", "ExamplePayload 2", "ExamplePayload 3"]