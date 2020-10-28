from colorama import Fore, Back, Style
import pytest


@pytest.yield_fixture()
def setUp():
    print(Fore.GREEN+"Running method level setUp")
    yield
    print(Fore.GREEN+"Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request):
    print(Fore.GREEN+"Running one time setUp - conftest.py file")
    if request.cls is not None:
        request.cls.driver
    yield
    print(Fore.GREEN+"Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")


import sys


def pytest_cmdline_preparse(args):
    if 'xdist' in sys.modules:  # pytest-xdist plugin
        import multiprocessing
        num = max(multiprocessing.cpu_count() / 2, 1)
        args[:] = ["-n", str(num)] + args
