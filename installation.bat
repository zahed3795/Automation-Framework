@ECHO OFF
python --version
pip install -r requirements.txt
python install setup.py
cd masterQA\utilities\selenium_grid
python download_selenium_server.py
cd..
cd..
cd..









