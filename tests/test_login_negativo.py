from pages.login_page import LoginPage #Importa la clase LoginPage desde esa localización
#Importo los usuarios de USERS.CSV para poder utilizarlos en el test de login
from data.users import USERS
import pytest #para utilizar la funcion de PARAMETRIZAR

@pytest.mark.negativo
def test_login_negativo(driver):
    login_page = LoginPage(driver) #Instancio la clase y le paso el driver como parámetro

    login_page.open()
    #No incluyo los datos de usuario ni contraseña para simular un login con campos vacíos
    login_page.enviar() #Llamo al método de hacer login para iniciar sesión

    # Verifico que se muestra un mensaje de error
    error_message = login_page.obtener_mensaje_error()
    assert "Epic sadface: Username is required" in error_message
    print("Mensaje de error en pantalla:", error_message)