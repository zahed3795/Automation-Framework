"""
You'll probably want to customize this to your own environment and needs.
"""


# #####>>>>>----- REQUIRED/IMPORTANT SETTINGS -----<<<<<#####
# #####>>>>>----- MasterQA SETTINGS -----<<<<<#####
# ##### (Used when importing MasterQA as the parent class)
# Default maximum time (in seconds) to wait for page elements to appear.
# Different methods/actions in base_case.py use different timeouts.
# If the element to be acted on does not appear in time, the test fails.
class environment:
    BROWSER = 'chrome'
    URL = 'https://finviz.com/'
    USERNAME = 'Use encryption'
    PASSWORD = ' Use encryption'
    MINI_TIMEOUT = 2
    IMPLICITLY_TIMEOUT = 20
    PAGE_LOAD_TIMEOUT = 20
    EXTREME_TIMEOUT = 30


# File Path For Runtime Creation
class Files:
    DOWNLOADS_FOLDER = "downloaded_files"
    ARCHIVED_DOWNLOADS_FOLDER = "archived_files"


# Time Out
SMALL_TIMEOUT = 5
MINI_TIMEOUT = 8
LARGE_TIMEOUT = 10
EXTREME_TIMEOUT = 12

# Default names for files saved during test failures.
# (These files will get saved to the "latest_logs/" folder.)
SCREENSHOT_NAME = "screenshot.png"
BASIC_INFO_NAME = "basic_test_info.txt"
PAGE_SOURCE_NAME = "page_source.html"

# Default names for files and folders saved when using nosetests reports.
# Usage: "--report". (NOSETESTS only)
LATEST_REPORT_DIR = "latest_report"
REPORT_ARCHIVE_DIR = "archived_reports"
HTML_REPORT = "report.html"
RESULTS_TABLE = "results_table.csv"

CHROME_START_WIDTH = 1250
CHROME_START_HEIGHT = 840
HEADLESS_START_WIDTH = 1440
HEADLESS_START_HEIGHT = 1880
ARCHIVE_EXISTING_DOWNLOADS = "archived_files"

# The default message that appears when you don't specify a custom message
MASTERQA_DEFAULT_VALIDATION_MESSAGE = "Does the page look good?"

# MySQL DB Credentials
# (For saving data from tests to a MySQL DB)
# Usage: "--with-db_reporting"
DB_HOST = "127.0.0.1"
DB_PORT = 3306
DB_USERNAME = "root"
DB_PASSWORD = "test"
DB_SCHEMA = "test_db"

# Amazon S3 Bucket Credentials
# (For saving screenshots and other log files from tests)
# (Bucket names are unique across all existing bucket names in Amazon S3)
# Usage: "--with-s3_logging"
S3_LOG_BUCKET = "[S3 BUCKET NAME]"
S3_BUCKET_URL = "https://s3.amazonaws.com/[S3 BUCKET NAME]/"
S3_SELENIUM_ACCESS_KEY = "[S3 ACCESS KEY]"
S3_SELENIUM_SECRET_KEY = "[S3 SECRET KEY]"

# ENCRYPTION SETTINGS
# (Used for string/password obfuscation)
# (You should reset the Encryption Key for every clone of SeleniumBase)
ENCRYPTION_KEY = "Pg^.l!8UdJ+Y7dMIe&fl*%!p9@ej]/#tL~3E4%6?"
# These tokens are added to the beginning and end of obfuscated passwords.
# Helps identify which strings/passwords have been obfuscated.
OBFUSCATION_START_TOKEN = "$^*ENCRYPT="
OBFUSCATION_END_TOKEN = "?&#$"
