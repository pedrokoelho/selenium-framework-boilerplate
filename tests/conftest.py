import pytest
from selenium import webdriver

@pytest.fixture()
def driver():

    # setup

    # using ChromeOptions
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    
    my_driver = webdriver.Chrome(options=options)
    
    # run tests
    yield my_driver

    # teardown
    my_driver.quit()