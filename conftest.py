import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://google.com")
    yield driver
    driver.close()
    driver.quit()
