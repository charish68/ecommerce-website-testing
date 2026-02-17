from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

def test_homepage_title():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://automationexercise.com")

    time.sleep(3)

    assert "Automation Exercise" in driver.title

    driver.quit()
