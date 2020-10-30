@ECHO OFF
python --version
py -m pip install --upgrade pip
pip install webdriver_manager==3.2.2
pip install pytest==6.1.1
pip install pytest-xdist==2.1.0
pip install parameterized==0.7.4
pip install cryptography==3.1.1
pip install urllib3==1.25.10
pip install requests==2.24.0
pip install pytest-json-report==1.2.1
pip install pytest-json==0.4.0
pip install openpyxl==3.0.5
pip install elementpath==2.0.3
pip install pytest-html-reporter==0.2.3
pip install pytest-bdd==4.0.1
pip install pytest-html==2.1.1
pip install -U requests Flask pytest pytest-html
pip install numpy==1.19.2
pip install selenium==3.141.0
pip install setuptools>=44.1.1
pip install -r requirements.txt
pip install importlib-metadata==2.0.0
pip install colorama==0.4.4
pip install urllib3==1.25.10
pip install cssselect==1.1.0
pip install pytest-html
pip install pytest-bdd==4.0.1
pip install pytest-bdd-web==0.1.1
py -m pip install --user virtualenv
pip install --user pipenv
pip install colorama
cd masterQA\utilities\selenium_grid
python download_selenium_server.py
cd..
cd..
cd..









