from automation.config.config import Config


def test_homepage_title(driver):
    driver.get(Config.BASE_URL)
    assert "Automation" in driver.title
