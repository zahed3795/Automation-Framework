"""
This module contains useful Javascript utility methods for base_case.py
These helper methods SHOULD NOT be called directly from tests.
"""
import re
import requests
import time
from selenium.common.exceptions import WebDriverException, NoSuchElementException


def clear_out_console_logs(driver):
    try:
        # Clear out the current page log before navigating to a new page
        # (To make sure that assert_no_js_errors() uses current results)
        driver.get_log('browser')
    except NoSuchElementException:
        pass
