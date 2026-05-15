from selenium.webdriver.common.by import By

# Función reutilizable de login. El driver se encuentra en la carpeta conftest.py como fixture
def login(driver):
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "/inventory.html" in driver.current_url
    print ("La URL contiene 'Inventory'")