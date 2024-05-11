import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='module', autouse=True)
def manage_browser():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless=new')
    browser.config.driver_options = options

    yield

    browser.quit()

