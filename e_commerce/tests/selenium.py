import pytest
from selenium import webdriver
from selenium.webdriver.safari.options import Options


@pytest.fixture(scope='module')
def safari_browser_instance(request):
    """
    provide a selenium webdriver instance
    """
    options = Options()
    options.headless = False
    browser = webdriver.Safari(safari_options=options)
    yield browser
    browser.close()
