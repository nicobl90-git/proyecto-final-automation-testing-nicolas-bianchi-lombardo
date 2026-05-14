import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.login
def test_login(chrome_driver):
    chrome_driver.get("https://www.saucedemo.com")
    chrome_driver.find_element(By.ID, "user-name").send_keys("standard_user")
    chrome_driver.find_element(By.ID, "password").send_keys("secret_sauce")
    chrome_driver.find_element(By.ID, "login-button").click()
    assert "/inventory.html" in chrome_driver.current_url
    print ("La URL contiene 'Inventory'")