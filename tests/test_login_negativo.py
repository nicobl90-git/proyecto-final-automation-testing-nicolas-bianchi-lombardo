from pages.login_page import LoginPage #Importa la clase LoginPage desde esa localización
#Importo los usuarios de USERS.CSV para poder utilizarlos en el test de login
from data.users import NOT_USERS
import pytest #para utilizar la funcion de PARAMETRIZAR

@pytest.mark.negativo
@pytest.mark.ui
def test_login_vacio(driver):
    login_page = LoginPage(driver) #Instancio la clase y le paso el driver como parámetro

    login_page.open()
    #No incluyo los datos de usuario ni contraseña para simular un login con campos vacíos
    login_page.enviar() #Llamo al método de hacer login para iniciar sesión

    # Verifico que se muestra un mensaje de error
    error_message = login_page.obtener_mensaje_error()
    assert "Epic sadface: Username is required" in error_message
    print("Mensaje de error en pantalla:", error_message)

@pytest.mark.negativo
@pytest.mark.ui
@pytest.mark.parametrize("username, password", NOT_USERS) #Utilizo la función de parametrizar para los datos de NOT_USERS 
def test_login_invalido(driver, username, password):
    login_page = LoginPage(driver) #Instancio la clase y le paso el driver como parámetro

    login_page.open()
    login_page.completar_usuario(username) #Llamo al usuario inválido
    login_page.completar_clave(password) #Llamo al password inválido
    login_page.enviar() #Llamo al método de hacer login para iniciar sesión

    # Verifico que se muestra un mensaje de error
    error_message = login_page.obtener_mensaje_error()
    assert "Epic sadface: Username and password do not match any user in this service" in error_message
    print("Mensaje de error en pantalla:", error_message)