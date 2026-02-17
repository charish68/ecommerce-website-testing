from automation.pages.login_page import LoginPage
from automation.config.config import Config


def test_login_with_invalid_credentials(driver):
    driver.get(Config.LOGIN_URL)

    login = LoginPage(driver)
    login.enter_email("wrong@test.com")
    login.enter_password("wrongpassword")
    login.click_login()

    assert "Your email or password is incorrect!" in driver.page_source
