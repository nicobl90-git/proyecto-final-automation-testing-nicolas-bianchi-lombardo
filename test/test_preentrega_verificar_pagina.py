import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.helpers import login

@pytest.mark.verificar_pagina
def test_verificar_pagina(chrome_driver):
    login(chrome_driver)
    wait = WebDriverWait(chrome_driver, 5)
    titulo_pagina = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".app_logo"))).text
    titulo_seccion = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".title[data-test='title']"))).text
    print(f"El título de la página es {titulo_pagina} y la sección es {titulo_seccion}")

@pytest.mark.verificar_pagina
def test_productos_visibles(chrome_driver):
    login(chrome_driver)
    wait = WebDriverWait(chrome_driver, 5)
    producto_nombre = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))).text
    producto_precio = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div"))).text
    print(f"Se encontró el siguiente producto: {producto_nombre} y su precio es {producto_precio}")

@pytest.mark.verificar_pagina
def test_elementos_interfaz(chrome_driver):
    login(chrome_driver)
    wait = WebDriverWait(chrome_driver, 5)
    assert wait.until(EC.visibility_of_element_located((By.ID, "react-burger-menu-btn")))
    print("Se encontró el menú sandwich")
    assert wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "select_container")))
    print("Se encontró el filtro para los productos")
    assert wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_container")))
    print("Se encontró el botón del carrito")