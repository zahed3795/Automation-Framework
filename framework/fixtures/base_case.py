import unittest
import codecs
import json
import logging
import math
import os
import re
import sys
import time
import urllib3
if not urllib3:
    raise Exception('Need to run installation.bat')

import unittest
from selenium.common.exceptions import (StaleElementReferenceException,
                                        MoveTargetOutOfBoundsException,
                                        WebDriverException,
                                        ElementClickInterceptedException)
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from framework.core import browser_launcher
from framework.data import settings
from framework.data.settings import environment as env
from framework.fixtures import page_utils, js_utils
from framework.fixtures import page_actions
from colorama import Fore, Back, Style

logging.getLogger("requests").setLevel(logging.ERROR)
logging.getLogger("urllib3").setLevel(logging.ERROR)
urllib3.disable_warnings()


class Base(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(Base, self).__init__(*args, **kwargs)
        self.driver = None
        if True:
            self.driver = browser_launcher.DriverInstance(env.BROWSER)
        self.__last_page_load_url = "data:,"

    def Open(self, URL):
        """ Navigates the current browser window to the specified page.
        Proper use self.Click('//a[contains(text(),"Screener")]', "xpath", delay=5)
        For slow click you can use 'delay=5' as parameter
        """
        if self.__looks_like_a_page_url(URL) or page_utils.is_valid_url():
            if type(URL) is str:
                URL = URL.strip()  # Remove leading and trailing whitespace
            if URL.startswith("://"):
                # Convert URLs such as "://google.com" into "https://google.com"
                URL = "https" + URL
            js_utils.clear_out_console_logs(self.driver)
            self.driver.get(URL)
        else:
            print('Your URL is not in correct format')

    # Element click
    def Click(self, locator, locatorType=None, delay=0):
        """ Click Function will help you to click any element """
        if not locatorType:
            locatorType = self._select_locator_type(locator)

        if delay and delay > 0:
            time.sleep(delay)
        try:
            element = self.getElement(locator, locatorType)
            try:
                element.click()
            except StaleElementReferenceException and WebDriverException:
                time.sleep(0.16)
                actions = self.KeyBoard()
                actions.move_to_element(element).perform()
                actions.click(element).perform()
        except ElementClickInterceptedException:
            print("Cannot click on the element with locator: " + str(locator) + " locatorType: " + str(locatorType))

    # Enter text - Send Keys
    def Send_Text(self, locator, text, locatorType=None):
        if not locatorType:
            locatorType = self._select_locator_type(locator)

        self.Clear_Textbox(locator)
        actions = self.KeyBoard()
        element = self.getElement(locator, locatorType)
        try:
            element.send_keys(text)
        except StaleElementReferenceException:
            page_actions.timeout()
            actions.move_to_element(element).perform()
            actions.click(element).perform()
            actions.click(element).send_keys(text).perform()

    def Replace_existing_text(self, locator, text, locatorType=None):
        if not locatorType:
            locatorType = self._select_locator_type(locator)

        self.Clear_Textbox(locator)
        actions = self.KeyBoard()
        element = self.getElement(locator, locatorType)
        try:
            element.send_keys(text)
        except StaleElementReferenceException:
            page_actions.timeout()
            actions.move_to_element(element).perform()
            actions.click(element).perform()
            actions.click(element).send_keys(text).perform()

    # Clear Text Box Data
    def Clear_Textbox(self, locator, locatorType=None):
        if not locatorType:
            locatorType = self._select_locator_type(locator)

        element = self.getElement(locator, locatorType)
        try:
            element.click()
            element.clear()
        except StaleElementReferenceException:
            try:
                page_actions.timeout()
                element.click()
                element.clear()
            except StaleElementReferenceException:
                actions = self.KeyBoard()
                actions.move_to_element(element).perform()
                for i in range(5):
                    actions.click(element).perform()
                    actions.send_keys(Keys.BACKSPACE * 5).perform()
                if not element.text == str(''):
                    try:
                        for i in range(20):
                            actions.send_keys(Keys.BACKSPACE).perform()
                    except ElementClickInterceptedException:
                        backspaces = Keys.BACK_SPACE * 20  # Is the answer to everything
                        actions.send_keys(backspaces).perform()

    def Submit(self, locator, locatorType=None, delay=0):
        """ Alternative to self.driver.find_element_by_*(SELECTOR).submit() """
        if not locatorType:
            locatorType = self._select_locator_type(locator)

        self.web_driver_wait(locator, locatorType)
        element = self.getElement(locator, locatorType)
        if delay and delay > 0:
            time.sleep(delay)
        try:
            element.submit()
        except StaleElementReferenceException:
            time.sleep(0.50)
            element.submit()

    def web_driver_wait(self, locator, locatorType=None, delay=None):
        if not locatorType:
            locatorType = self._select_locator_type(locator)
        byType = self.getByType(locatorType)

        if not delay:
            delay = settings.SMALL_TIMEOUT

        wait = WebDriverWait(self.driver, delay).until(
            expected_conditions.visibility_of_element_located((byType, locator)))
        return wait

    # Double click element
    def Double_Click(self, locator, locatorType=None):
        if not locatorType:
            locatorType = self._select_locator_type(locator)

        actions = self.KeyBoard()
        element = self.getElement(locator, locatorType)
        try:
            actions.double_click(element).perform()
        except StaleElementReferenceException or WebDriverException:
            page_actions.timeout(2)
            actions.double_click(element).perform()

    def KeyBoard(self):
        """This Function Represent ActionChains Class """
        actions = ActionChains(self.driver)
        return actions

    def Press_Enter(self):
        """This Function Press ENTER Key From KeyBoard"""
        ENTER = self.KeyBoard().send_keys(Keys.ENTER)
        try:
            ENTER.perform()
        except StaleElementReferenceException:
            page_actions.timeout()
            ENTER.perform()

    def Full_Screen(self):
        """This Function Maximize Browser"""
        if self.driver.minimize_window() or not self.driver.fullscreen_window():
            return self.driver.fullscreen_window()

    def Maximize_wendow(self):
        # Maximize the window
        if not self.driver.maximize_window():
            return self.driver.maximize_window()

    def Minimize_Screen(self):
        """This Function Minimize Browser """
        if not self.driver.minimize_window():
            return self.driver.minimize_window()

    def Scroll_Into_View(self, locator, locatorType=None):
        """This Function Will scroll element into view"""
        if not locatorType:
            locatorType = self._select_locator_type(locator)

        element = self.getElement(locator, locatorType)
        actions = self.KeyBoard()
        try:
            actions.move_to_element(element).perform()
        except StaleElementReferenceException or MoveTargetOutOfBoundsException or ElementClickInterceptedException:
            page_actions.timeout(0.17)
            actions.move_to_element(element).perform()

    def Select_by_visible_text(self, visible_text, locator, locatorType=None):
        if not locatorType:
            locatorType = self._select_locator_type(locator)

        byType = self.getByType(locatorType)
        wait = WebDriverWait(self.driver, settings.SMALL_TIMEOUT)
        element = wait.until(expected_conditions.visibility_of_element_located((byType, locator)))
        select = Select(element)
        select.select_by_index(visible_text)
        if True:
            print(Fore.GREEN + str(visible_text) + " was selected for " + str(locator))

    def Select_by_index(self, index, locator, locatorType=None):
        if not locatorType:
            locatorType = self._select_locator_type(locator)
        byType = self.getByType(locatorType)
        wait = WebDriverWait(self.driver, settings.SMALL_TIMEOUT)
        element = wait.until(expected_conditions.visibility_of_element_located((byType, locator)))
        select = Select(element)
        select.select_by_index(index)
        if True:
            print(Fore.GREEN + str(index) + " was selected for " + str(locator))

    def Select_by_value(self, value, locator, locatorType=None):
        if not locatorType:
            locatorType = self._select_locator_type(locator)

        byType = self.getByType(locatorType)
        wait = WebDriverWait(self.driver, settings.SMALL_TIMEOUT)
        element = wait.until(expected_conditions.visibility_of_element_located((byType, locator)))
        select = Select(element)
        select.select_by_value(value)
        if True:
            print(Fore.GREEN + str(value) + " was selected for " + str(locator))

    def Refresh_page(self, delay=0):
        # If the ad_block feature is enabled, then block ads for new URLs
        current_url = self.driver.current_url
        if not current_url == self.__last_page_load_url:
            URL = self.driver.get(current_url)
            if delay and delay > 0:
                time.sleep(delay)
            time.sleep(0.10)
            self.driver.refresh()
            return URL

    def Get_current_url(self):
        current_url = self.driver.current_url
        if "%" in current_url and sys.version_info[0] >= 3:
            try:
                from urllib.parse import unquote
                current_url = unquote(current_url, errors='strict')
            except WebDriverException:
                pass
        return current_url

    def Get_page_title(self):
        """Return Page Title"""
        try:
            title = self.driver.title
        except StaleElementReferenceException:
            time.sleep(0.30)
            title = self.driver.title
        return title

    def get_user_agent(self):
        user_agent = self.driver.execute_script("return navigator.userAgent;")
        return user_agent

    def get_locale_code(self):
        locale_code = self.driver.execute_script(
            "return navigator.language || navigator.languages[0];")
        return locale_code

    def set_window_rect(self, x, y, width, height):
        self.driver.set_window_rect(x, y, width, height)

    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)

    def switch_to_default_window(self):
        self.driver.switch_to_window(0)

    def switch_to_driver(self, driver):
        """ Sets self.driver to the specified driver.
            You may need this if using self.get_new_driver() in your code. """
        self.driver = driver

    def get_beautiful_soup(self, source=None):
        """ BeautifulSoup is a toolkit for dissecting an HTML document
            and extracting what you need. It's great for screen-scraping! """
        from bs4 import BeautifulSoup
        if not source:
            source = self.driver.page_source
        soup = BeautifulSoup(source, "html.parser")
        return soup

    def get_unique_links(self):
        """ Get all unique links in the html of the page source.
            Page links include those obtained from:
            "a"->"href", "img"->"src", "link"->"href", and "script"->"src". """
        page_url = self.driver.current_url
        soup = self.get_beautiful_soup(self.driver.page_source)
        links = page_utils._get_unique_links(page_url, soup)
        return links

    def print_unique_links_with_status_codes(self):
        """ Finds all unique links in the html of the page source
            and then prints out those links with their status codes.
            Format:  ["link"  ->  "status_code"]  (per line)
            Page links include those obtained from:
            "a"->"href", "img"->"src", "link"->"href", and "script"->"src". """
        page_url = self.Get_current_url()
        soup = self.get_beautiful_soup(self.driver.page_source)
        page_utils._print_unique_links_with_status_codes(page_url, soup)

    def Download_file(self, file_url, destination_folder=None):
        """ Downloads the file from the url to the destination folder.
            If no destination folder is specified, the default one is used.
            (The default downloads folder = "./dowonload_folder") """
        abs_path = os.path.abspath('.')
        if not destination_folder:
            destination_folder = os.path.join(abs_path, "dowonload_folder")
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        page_utils._download_file_to(file_url, destination_folder)

    def save_file_as(self, file_url, new_file_name, destination_folder=None):
        """ Similar to self.download_file(), except that you get to rename the
            file being downloaded to whatever you want. """
        abs_path = os.path.abspath('.')
        if not destination_folder:
            destination_folder = os.path.join(abs_path, "dowonload_folder")
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        page_utils._download_file_to(
            file_url, destination_folder, new_file_name)

    def save_data_as(self, data, file_name, destination_folder=None):
        """ Saves the data specified to a file of the name specified.
            If no destination folder is specified, the default one is used.
            (The default downloads folder = "./downloaded_files") """
        abs_path = os.path.abspath('.')
        if not destination_folder:
            destination_folder = os.path.join(abs_path, "dowonload_folder")
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        page_utils._save_data_as(data, destination_folder, file_name)

    def __looks_like_a_page_url(self, url):
        """ Returns True if the url parameter looks like a URL. This method
            is slightly more lenient than page_utils.is_valid_url(url) due to
            possible typos when calling self.get(url), which will try to
            navigate to the page if a URL is detected, but will instead call
            self.get_element(URL_AS_A_SELECTOR) if the input in not a URL. """
        if (url.startswith("http:") or url.startswith("https:") or (
                url.startswith("://") or url.startswith("chrome:") or (
                url.startswith("about:") or url.startswith("data:") or (
                url.startswith("file:") or url.startswith("edge:") or (
                url.startswith("opera:")))))):
            return True
        else:
            return False

    def _select_locator_type(self, locator, locatorType=None):
        # If locatorType does not mention, below code will run
        if not locatorType:
            if page_utils.is_xpath_selector(locator):
                locatorType = 'xpath'
            elif page_utils.is_link_text_selector():
                locatorType = 'link'
            elif page_utils.is_name_selector():
                locatorType = 'name'
            else:
                locatorType = 'css'
            return locatorType
        return False

    # Element by type
    def getByType(self, locatorType):

        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            print("Locator type " + locatorType + " not correct/supported")
        return False

    # Get element
    def getElement(self, locator, locatorType):
        locatorType = locatorType.lower()
        byType = self.getByType(locatorType)
        element = self.driver.find_element(byType, locator)
        return element

    @classmethod
    def setUpClass(cls):
        print(Fore.GREEN)

    @classmethod
    def tearDownClass(cls):
        print(Fore.GREEN)
