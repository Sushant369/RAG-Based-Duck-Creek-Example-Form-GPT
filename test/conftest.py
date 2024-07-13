from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager 


import pytest
# import time as t
from app import *  # E


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Send 'chrome' as parameter for execution"
    )

@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    driver = ""

    options = Options()
    options.add_argument("--headless")
    
    if browser == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

