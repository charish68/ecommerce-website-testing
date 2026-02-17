from automation.config.config import Config

class WaitUtils:

    def __init__(self, driver, timeout=Config.TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
