import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.agregar_carrito
def test_agregar_producto(chrome_driver):
    wait = WebDriverWait(chrome_driver, 5)
    chrome_driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    cantidad_carrito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))).text
    assert cantidad_carrito == "1"
    print(f"El carrito muestra el número {cantidad_carrito}")
    chrome_driver.find_element(By.CLASS_NAME, "shopping_cart_container").click()
    producto_carrito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))).text
    assert producto_carrito == "Sauce Labs Backpack"
    print(f"El producto que se encuentra en el carrito es {producto_carrito}")