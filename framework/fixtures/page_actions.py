"""
This module contains a set of methods that can be used for page loads and
for waiting for elements to appear on a page.
"""

import codecs
import os
import sys
import time
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common import exceptions as selenium_exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.errorhandler import ElementNotVisibleException
from selenium.webdriver.remote.errorhandler import NoSuchElementException
from selenium.webdriver.remote.errorhandler import NoAlertPresentException
from selenium.webdriver.remote.errorhandler import NoSuchFrameException
from selenium.webdriver.remote.errorhandler import NoSuchWindowException
from framework.data import settings
from framework.fixtures import page_utils


def timeout(secToWait=None):
    if not secToWait:
        time.sleep(settings.SMALL_TIMEOUT)
    else:
        time.sleep(secToWait)
