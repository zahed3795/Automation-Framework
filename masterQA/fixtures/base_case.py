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
from masterQA.core import browser_launcher
from masterQA.data import settings
from masterQA.data.settings import environment as env
from masterQA.fixtures import page_utils
from masterQA.fixtures import page_actions as ps
from colorama import Fore, Back, Style

logging.getLogger("requests").setLevel(logging.ERROR)
logging.getLogger("urllib3").setLevel(logging.ERROR)
urllib3.disable_warnings()


class BaseCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(BaseCase, self).__init__(*args, **kwargs)
        self.driver = None
        if True:
            self.driver = browser_launcher.DriverInstance(env.BROWSER)

    def Open(self, URL):
        """ Navigates the current browser window to the specified page. """
        if type(URL) is str:
            URL = URL.strip()  # Remove leading and trailing whitespace
        if URL.startswith("://"):
            # Convert URLs such as "://google.com" into "https://google.com"
            URL = "https" + URL
        self.driver.get(URL)

    # Element click
    def Click(self, locator, locatorType=None):
        """ Click Function will help you to click any element """
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
        try:
            element = self.getElement(locator, locatorType)
            try:
                element.click()
            except StaleElementReferenceException and WebDriverException:
                ps.timeout(2)
                actions = self.KeyBoard()
                actions.move_to_element(element).perform()
                actions.click(element).perform()
        except:
            print("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)

    # Enter text - Send Keys
    def Send_Text(self, locator, text, locatorType=None):
        if not locatorType:
            if page_utils.is_xpath_selector(locator):
                locatorType = 'xpath'
            elif page_utils.is_link_text_selector():
                locatorType = 'link'
            elif page_utils.is_name_selector():
                locatorType = 'name'
            else:
                locatorType = 'css'
        self.Clear_Textbox(locator)
        actions = self.KeyBoard()
        element = self.getElement(locator, locatorType)
        try:
            element.send_keys(text)
        except StaleElementReferenceException:
            ps.timeout()
            actions.move_to_element(element).perform()
            actions.click(element).perform()
            actions.click(element).send_keys(text).perform()

    # Clear Text Box Data
    def Clear_Textbox(self, locator, locatorType=None):
        if not locatorType:
            if page_utils.is_xpath_selector(locator):
                locatorType = 'xpath'
            elif page_utils.is_link_text_selector():
                locatorType = 'link'
            elif page_utils.is_name_selector():
                locatorType = 'name'
            else:
                locatorType = 'css'
        element = self.getElement(locator, locatorType)
        try:
            element.click()
            element.clear()
        except StaleElementReferenceException:
            try:
                ps.timeout()
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

    # Clear Text Box Data
    def Dobul_Click(self, locator, locatorType):
        actions = self.KeyBoard()
        element = self.getElement(locator, locatorType)
        try:
            actions.double_click(element).perform()
        except StaleElementReferenceException and WebDriverException:
            ps.timeout(2)
            actions.double_click(element).perform()

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
            ps.timeout()
            ENTER.perform()

    def Full_Screen(self):
        """This Function Maximize Browser"""
        if self.driver.minimize_window() or not self.driver.fullscreen_window():
            return self.driver.fullscreen_window()

    def Minimize_Screen(self):
        """This Function Minimize Browser """
        if not self.driver.minimize_window():
            return self.driver.minimize_window()

    def Scroll_Into_View(self, locator, locatorType=None):
        """This Function Will scroll element into view"""
        if not locatorType:
            if page_utils.is_xpath_selector(locator):
                locatorType = 'xpath'
            elif page_utils.is_link_text_selector():
                locatorType = 'link'
            elif page_utils.is_name_selector():
                locatorType = 'name'
            else:
                locatorType = 'css'
        element = self.getElement(locator, locatorType)
        actions = self.KeyBoard()
        try:
            actions.move_to_element(element).perform()
        except StaleElementReferenceException:
            actions.move_to_element(element).perform()

    def Select_by_visible_text(self, visible_text, locator, locatorType=None):
        if not locatorType:
            if page_utils.is_xpath_selector(locator):
                locatorType = 'xpath'
            elif page_utils.is_link_text_selector():
                locatorType = 'link'
            elif page_utils.is_name_selector():
                locatorType = 'name'
            else:
                locatorType = 'css'
        byType = self.getByType(locatorType)
        wait = WebDriverWait(self.driver, settings.SMALL_TIMEOUT)
        element = wait.until(expected_conditions.visibility_of_element_located((byType, locator)))
        select = Select(element)
        select.select_by_index(visible_text)
        if True:
            print(Fore.GREEN + str(visible_text )+ " was selected for " + str(locator))
        else:
            select.deselect_by_index(index)
            select.select_by_index(visible_text)

    def Select_by_index(self, index, locator, locatorType=None):
        if not locatorType:
            if page_utils.is_xpath_selector(locator):
                locatorType = 'xpath'
            elif page_utils.is_link_text_selector():
                locatorType = 'link'
            elif page_utils.is_name_selector():
                locatorType = 'name'
            else:
                locatorType = 'css'
        byType = self.getByType(locatorType)
        wait = WebDriverWait(self.driver, settings.SMALL_TIMEOUT)
        element = wait.until(expected_conditions.visibility_of_element_located((byType, locator)))
        select = Select(element)
        select.select_by_index(index)
        if True:
            print(Fore.GREEN + str(index) + " was selected for " + str(locator))
        else:
            select.deselect_by_index(index)
            select.select_by_index(index)

    def Select_by_value(self, value, locator, locatorType=None):
        if not locatorType:
            if page_utils.is_xpath_selector(locator):
                locatorType = 'xpath'
            elif page_utils.is_link_text_selector():
                locatorType = 'link'
            elif page_utils.is_name_selector():
                locatorType = 'name'
            else:
                locatorType = 'css'
        byType = self.getByType(locatorType)
        wait = WebDriverWait(self.driver, settings.SMALL_TIMEOUT)
        element = wait.until(expected_conditions.visibility_of_element_located((byType, locator)))
        select = Select(element)
        select.select_by_value(value)
        if True:
            print(Fore.GREEN + str(value) + " was selected for " + str(locator))
        else:
            select.deselect_by_value(index)
            select.select_by_value(index)

    def Driver_tear_Down(self):
        return self.driver.close()

    @classmethod
    def setUpClass(cls):
        print(Fore.GREEN)

    @classmethod
    def tearDownClass(cls):
        print(Fore.GREEN)
