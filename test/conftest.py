import pytest

#Voy a traer los fixtures que se encuentran en el archivo preentrega.py para poder utilizarlos en los tests.
#En este caso, voy a dejar solamente el fixture para el driver. En el archivo helpers.py dejaré la función de login. 

from selenium import webdriver #utilizo el driver para despues guardarlo en una variable
from webdriver_manager.chrome import ChromeDriverManager #Traigo el driver para el navegador que quiero trabajar
from selenium.webdriver.chrome.service import Service #Este servicio recibe el chrome driver manager y me instala la version correcta segun mi navegador
from selenium.webdriver.common.by import By

@pytest.fixture
def chrome_driver(): #creo una función para el driver
    service = Service(ChromeDriverManager().install()) #descarga el driver automáticameente y lo instala
    driver = webdriver.Chrome(service=service) #abre el navegador de Chrome
    yield driver #devuelve el driver para que pueda ser utilizado en los tests
    driver.quit() #cierra el navegador


