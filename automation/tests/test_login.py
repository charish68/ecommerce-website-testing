import json
import os
import pytest
from automation.pages.login_page import LoginPage
from automation.config.config import Config


def load_test_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "test_data", "login_data.json")

    with open(file_path) as f:
        return json.load(f)


@pytest.mark.parametrize("data", load_test_data())
def test_login_with_invalid_credentials(driver, data):
    driver.get(Config.LOGIN_URL)

    login = LoginPage(driver)
    login.enter_email(data["email"])
    login.enter_password(data["password"])
    login.click_login()

    assert "Your email or password is incorrect!" in driver.page_source
