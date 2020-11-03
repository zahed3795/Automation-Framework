import os
import sys

import requests
import urllib3
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium.common.exceptions import WebDriverException
from framework import drivers
from framework.data.settings import environment as env
from webdriver_manager.driver import ChromeDriver
from webdriver_manager.utils import download_file, save_file, ChromeType
from colorama import Fore, Back, Style
urllib3.disable_warnings()
DRIVER_DIR = os.path.dirname(os.path.realpath(drivers.__file__))
PLATFORM = sys.platform
IS_WINDOWS = False
LOCAL_CHROMEDRIVER = None
LOCAL_GECKODRIVER = None
LOCAL_EDGEDRIVER = None
LOCAL_IEDRIVER = None
LOCAL_OPERADRIVER = None
os.system('cmd /c "color a"')
if not os.environ["PATH"].startswith(DRIVER_DIR):
    # Remove existing Framework DRIVER_DIR from System PATH if present
    os.environ["PATH"] = os.environ["PATH"].replace(DRIVER_DIR, "")
    # If two path separators are next to each other, replace with just one
    os.environ["PATH"] = os.environ["PATH"].replace(
        os.pathsep + os.pathsep, os.pathsep)
    # Put the SeleniumBase DRIVER_DIR at the beginning of the System PATH
    os.environ["PATH"] = DRIVER_DIR + os.pathsep + os.environ["PATH"]
if "win32" in PLATFORM:
    IS_WINDOWS = True
    LOCAL_EDGEDRIVER = DRIVER_DIR + '/msedgedriver.exe'
    LOCAL_IEDRIVER = DRIVER_DIR + '/IEDriverServer.exe'
    LOCAL_CHROMEDRIVER = DRIVER_DIR + '/chromedriver.exe'
    LOCAL_GECKODRIVER = DRIVER_DIR + '/geckodriver.exe'
    LOCAL_OPERADRIVER = DRIVER_DIR + '/operadriver.exe'


def DriverInstance(browser):
    """
    Get WebDriver Instance based on the browser configuration

    :return 'WebDriver Instance':
    """
    # Will open Opera Driver if XML ``browser``value set as FireFox else Chrome will be default driver
    if browser.lower() == "firefox" or browser.lower() == 'ff':
        try:
            if os.path.exists(LOCAL_GECKODRIVER):
                driver = webdriver.Firefox(executable_path=LOCAL_GECKODRIVER)
            else:
                latest = "https://api.github.com/repos/mozilla/geckodriver/releases/latest"
                url_request = requests.get(latest)
                if url_request.ok:
                    use_version = url_request.json()["tag_name"]
                    file = download_file("https://github.com/mozilla/geckodriver/"
                                         "releases/download/" + use_version + "/geckodriver-" + use_version + "-"
                                         + "win64" + ".zip")
                    archive = save_file(file, DRIVER_DIR)
                    archive.unpack(DRIVER_DIR)
                    if os.path.exists(LOCAL_GECKODRIVER):
                        driver = webdriver.Firefox(executable_path=LOCAL_GECKODRIVER)
                    # https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-win64.zip
            if os.path.exists(DRIVER_DIR + '/geckodriver-v0.27.0-win64.zip'):
                os.remove(DRIVER_DIR + "/geckodriver-v0.27.0-win64.zip")
            print(Fore.GREEN+' FireFox running as driver')

        except WebDriverException:
            driver = webdriver.Firefox(GeckoDriverManager().install())

            # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    # Will open Opera Driver if XML ``browser``value set as chrome else Chrome will be default driver
    elif browser.lower() == "chrome":
        # Set Chrome driver
        if os.path.exists(LOCAL_CHROMEDRIVER):
            driver = webdriver.Chrome(executable_path=LOCAL_CHROMEDRIVER)

        else:
            latest = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
            url_request = requests.get(latest)
            use_version = url_request.text
            file = download_file("http://chromedriver.storage.googleapis.com/"+use_version+"/chromedriver_win32.zip")
            archive = save_file(file, DRIVER_DIR)
            archive.unpack(DRIVER_DIR)

            if os.path.exists(LOCAL_CHROMEDRIVER):
                driver = webdriver.Chrome(executable_path=LOCAL_CHROMEDRIVER)
            else:
                driver = webdriver.Chrome(ChromeDriverManager().install())
        print(Fore.GREEN + ' Chrome running as driver')
    # Will open Opera Driver if XML ``browser``value set as IE else Chrome will be default driver
    elif browser.lower() == 'ie':
        try:
            driver = webdriver.Ie(executable_path=LOCAL_IEDRIVER)
        except WebDriverException:
            driver = webdriver.Ie(IEDriverManager(path=DRIVER_DIR).install())
            # driver = webdriver.Ie(IEDriverManager().install())
    # Will open Opera Driver if XML ``browser``value set as Edge else Chrome will be default driver
    elif browser.lower() == 'edge':
        if os.path.exists(LOCAL_EDGEDRIVER):
            driver = webdriver.Edge(executable_path=LOCAL_EDGEDRIVER)
        else:
            latest = (
                "https://msedgewebdriverstorage.blob.core.windows.net"
                "/edgewebdriver/LATEST_STABLE")
            latest = requests.get(latest)
            if latest.ok:
                use_version = latest.text.split('\r')[0].split('\n')[0]
                file = download_file(
                    "https://msedgedriver.azureedge.net/" + use_version + "/edgedriver_" + PLATFORM + ".zip")
                archive = save_file(file, DRIVER_DIR)
                archive.unpack(DRIVER_DIR)

                if os.path.exists(LOCAL_EDGEDRIVER):
                    driver = webdriver.Edge(executable_path=LOCAL_EDGEDRIVER)
                else:
                    driver = webdriver.Edge(EdgeChromiumDriverManager(path=DRIVER_DIR).install())

            # driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        print(Fore.GREEN+' Edge running as driver')
    # Will open Opera Driver if XML ``browser``value set as Opera else Chrome will be default driver
    elif browser.lower() == 'opera':
        try:
            driver = webdriver.Opera(executable_path=LOCAL_OPERADRIVER)
        except WebDriverException:
            driver = webdriver.Opera(OperaDriverManager(path=DRIVER_DIR).install())

    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    if os.path.exists(DRIVER_DIR + '//drivers.json'):
        os.remove(DRIVER_DIR + '//drivers.json')
    if os.path.exists(DRIVER_DIR + "//driver.zip"):
        os.remove(DRIVER_DIR + "//driver.zip")
    # Setting Driver Implicit Time out for An Element
    driver.implicitly_wait(env.IMPLICITLY_TIMEOUT)
    # Setting Driver Page Load Time out for An Element
    driver.set_page_load_timeout(env.PAGE_LOAD_TIMEOUT)
    # Delete All Cookies
    driver.delete_all_cookies()
    # Functions returning driver
    return driver
