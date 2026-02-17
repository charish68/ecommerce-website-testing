from selenium.webdriver.common.by import By
from .base_page import BasePage
from automation.utils.wait_utils import WaitUtils
from automation.utils.logger import get_logger


class LoginPage(BasePage):

    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Login']")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WaitUtils(driver)
        self.logger = get_logger(self.__class__.__name__)

    def enter_email(self, email):
        self.logger.info("Entering email")
        self.wait.wait_for_element(self.EMAIL_INPUT).send_keys(email)

    def enter_password(self, password):
        self.logger.info("Entering password")
        self.wait.wait_for_element(self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.logger.info("Clicking login button")
        self.wait.wait_for_element(self.LOGIN_BUTTON).click()
