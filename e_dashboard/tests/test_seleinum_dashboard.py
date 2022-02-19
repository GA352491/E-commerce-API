import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.mark.selenium
def test_dashboard_admin_login(live_server, safari_browser_instance):
    browser = safari_browser_instance
    browser.get(("%s%s" % (live_server.url, "/admin/login")))
    user_name = browser.find_element(By.NAME, "username")
    user_password = browser.find_element(By.NAME, "password")
    submit = browser.find_element(By.XPATH, '//input@value="Log in"]')
    user_name.send_keys("root")
    user_password.send_keys("root")
    submit.send_keys(Keys.RETURN)

    assert "site administration" in browser.page_source