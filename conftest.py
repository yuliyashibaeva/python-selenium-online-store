import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='Choose the browser: chrome or firefox')
    parser.addoption('--headless', action='store_true', default=False,
                     help='whether to run the tests in a headless browser mode')


@pytest.fixture(scope="function")
def browser(request):
    browser_type = request.config.getoption("browser")
    headless = request.config.getoption("headless")

    if browser_type == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("headless")
        browser = webdriver.Chrome(options=options)
    elif browser_type == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("headless")
        browser = webdriver.Firefox(options=options)

    browser.implicitly_wait(10)
    yield browser
    browser.quit()
