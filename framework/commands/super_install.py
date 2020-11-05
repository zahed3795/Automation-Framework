"""
Installs the specified web driver.
    sdet install chrome
"""

import colorama
import os
import platform
import requests
import shutil
import sys
import tarfile
import urllib3
import zipfile
from framework import drivers  # webdriver storage folder for Super framework
from framework.core import browser_launcher

urllib3.disable_warnings()
DRIVER_DIR = os.path.dirname(os.path.realpath(drivers.__file__))


def invalid_run_command():
    exp = "  ** install **\n\n"
    exp += "  Example:\n"
    exp += "          sdet install chrome\n"
    exp += "  Output:\n"
    exp += "          Installs the chosen webdriver to framework/drivers/\n"
    exp += "          (chromedriver is required for Chrome automation)\n"
    exp += "          (geckodriver is required for Firefox automation)\n"
    exp += "          (edgedriver is required for Microsoft Edge automation)\n"
    exp += "          (iedriver is required for InternetExplorer automation)\n"
    exp += "          (operadriver is required for Opera Browser automation)\n"
    print("")
    raise Exception('INVALID RUN COMMAND!\n\n%s' % exp)


def make_executable(file_path):
    # Set permissions to: "If you can read it, you can execute it."
    mode = os.stat(file_path).st_mode
    mode |= (mode & 0o444) >> 2  # copy R bits to X
    os.chmod(file_path, mode)


def main():
    num_args = len(sys.argv)
    if sys.argv[0].split('/')[-1].lower() == "sdet" or (
            sys.argv[0].split('\\')[-1].lower() == "sdet") or (
            sys.argv[0].split('/')[-1].lower() == "qa") or (
            sys.argv[0].split('\\')[-1].lower() == "qa") or (
            sys.argv[0].split('/')[-1].lower() == "zahed") or (
            sys.argv[0].split('\\')[-1].lower() == "zahed"):
        if num_args < 3 or num_args > 5:
            invalid_run_command()
    else:
        invalid_run_command()
    name = sys.argv[2].lower()

    colorama.init(autoreset=True)
    c1 = colorama.Fore.MAGENTA + colorama.Back.GREEN
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTMAGENTA_EX
    c3 = colorama.Fore.GREEN + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL

    if name == "chrome" or name == "c":
        browser_launcher.DriverInstance(name)
        print('chrome downloaded')
    elif name == "firefox" or name == "ff" or name == "f":
        browser_launcher.DriverInstance(name)
    elif name == "opera" or name == "o":
        browser_launcher.DriverInstance(name)
    elif name == "edge" or name == "e":
        browser_launcher.DriverInstance(name)
    elif name == "ie" or name == "i":
        browser_launcher.DriverInstance(name)


if __name__ == "__main__":
    main()
