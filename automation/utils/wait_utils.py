from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from automation.config.config import Config


class WaitUtils:

    def __init__(self, driver, timeout=Config.TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
