"""
This module contains a set of methods that can be used for page loads and
for waiting for elements to appear on a page.

These methods improve on and expand existing WebDriver commands.
Improvements include making WebDriver commands more robust and more reliable
by giving page elements enough time to load before taking action on them.

The default option for searching for elements is by CSS Selector.
This can be changed by overriding the "By" parameter.
Options are:
By.CSS_SELECTOR
By.CLASS_NAME
By.ID
By.NAME
By.LINK_TEXT
By.XPATH
By.TAG_NAME
By.PARTIAL_LINK_TEXT
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
from masterQA.data import settings
from masterQA.fixtures import page_utils


def timeout(secToWait=None):
    if not secToWait:
        time.sleep(settings.SMALL_TIMEOUT)
    else:
        time.sleep(secToWait)
