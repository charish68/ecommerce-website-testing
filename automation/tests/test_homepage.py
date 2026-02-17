from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from automation.pages.home_page import HomePage

def test_homepage_title():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://automationexercise.com")

    home = HomePage(driver)
    assert "Automation Exercise" in home.get_title()

    driver.quit()
