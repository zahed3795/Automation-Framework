import time

import pytest
import os


def pytest_sessionfinish():
    print("*** test run reporting finishing")


class MyPlugin:
    pass


pytest.main(["-s", '-v', '--junitxml=Reports/report.xml', '--html=Reports/report.html'], plugins=[MyPlugin()])

Report = os.path.dirname(os.path.realpath(__file__))
HTML_Report = Report + "/pytest_html_report.html"
if os.path.exists(HTML_Report):
    time.sleep(1)
    os.remove(HTML_Report)
latest_logs = os.path.dirname(os.path.realpath(__file__))
rchived_logs = os.path.dirname(os.path.realpath(__file__))
archive = os.path.dirname(os.path.realpath(__file__))
archive2 = os.path.dirname(os.path.realpath(__file__))
archive = archive + "\\archive"
archive2 = archive2 + "\\archive\\output_160425****"
if os.path.exists(archive):
    for i in range(3):
        if os.path.exists(archive2):
            os.remove(archive2)
    os.rmdir(archive)
rchived_logs = rchived_logs + "/archived_logs"
if os.path.exists(rchived_logs):
    os.rmdir(rchived_logs)
latest_logs = latest_logs + "\latest_logs"
if os.path.exists(latest_logs):
    os.rmdir(latest_logs)
JSON_Report = Report + "/output.json"
if os.path.exists(JSON_Report):
    time.sleep(1)
    os.remove(JSON_Report)
assets = os.path.dirname(os.path.realpath(__file__))
assets = assets + "\\Reports\\assets"
if os.path.exists(assets):
    time.sleep(1)
    style = os.path.dirname(os.path.realpath(__file__))
    style = style + "\\Reports\\assets\\style.css"
    if os.path.exists(style):
        os.remove(style)
    os.rmdir(assets)

Report3 = os.path.dirname(os.path.realpath(__file__))
Report3 = Report3 + "\\Demo_web_test\\pytest_html_report.html"
if os.path.exists(Report3):
    os.remove(Report3)
JSON_Report2 = os.path.dirname(os.path.realpath(__file__))
JSON_Report2 = JSON_Report2 + "\\Demo_web_test\\output.json"
if os.path.exists(JSON_Report2):
    os.remove(JSON_Report2)
