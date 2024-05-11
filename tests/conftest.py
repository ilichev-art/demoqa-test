import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='module', autouse=True)
def manage_browser():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.window_height = 1080
    browser.config.window_width = 1366
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    options.add_argument('--headless=new')
    browser.config.driver_options = options

    yield

    browser.quit()

