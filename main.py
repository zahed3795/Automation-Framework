import pytest
import os


def pytest_sessionfinish():
    print("*** test run reporting finishing")


class MyPlugin:
    pass


pytest.main(["-s", '-v','-n 2', '--junitxml=Report/report.xml', '--html=Reports/report.html'], plugins=[MyPlugin()])
