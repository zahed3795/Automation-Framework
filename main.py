import pytest
import os


def pytest_sessionfinish():
    print("*** test run reporting finishing")


class MyPlugin:
    pass


pytest.main(["-s", '-v', '-n 2', '--junitxml=Reports/report.xml', '--html=Reports/report.html'], plugins=[MyPlugin()])

Report = os.path.dirname(os.path.realpath(__file__))
HTML_Report = Report + "/pytest_html_report.html"
if os.path.exists(HTML_Report):
    os.remove(HTML_Report)
JSON_Report = Report + "/output.json"
if os.path.exists(JSON_Report):
    os.remove(JSON_Report)
