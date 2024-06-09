import pytest
from dotenv import load_dotenv
import os
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach


def pytest_addoption(parser):
    parser.addoption(
        "--browser_version",
        default="100.0",
    )

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function")
def setup_browser(request):
    browser_version = request.config.getoption("--browser_version")
    options = Options()
    selenoid_capabilities = {
        "browserName": 'chrome',
        "browserVersion": browser_version,
        "selenoid:options": {"enableVideo": True, "enableVNC": True},
    }

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options,
    )
    browser.config.driver = driver

    browser.config.base_url = "https://demoqa.com"
    browser.config.window_width = int(os.getenv("selene.window_width", 1920))
    browser.config.window_height = int(os.getenv("selene.window_height", 1200))

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
