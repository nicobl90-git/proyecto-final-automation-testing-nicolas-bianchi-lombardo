## Propósito del proyecto
Este proyecto tiene como propósito la automatización de ciertas pruebas sobre funcionalidades esenciales del sitio www.saucedemo.com 
Estas pruebas consisten en la automatización del Login, la verificación de ciertos elementos de la página y agregar un producto al carrito, además de su corroboración. 

## Tecnologías utilizadas
- Lenguaje Python
- Selenium (framework para automatización en navegadores)
- Pytest (para automatizar casos de testing)
- Pytest-html (para generar reportes)
- ChromeDriver /webdriver manager (para navegar por Chrome)
- Devtools (para la localización de selectores CSS para los elementos pertinentes, utilizando atributos y clases por ejemplo, ID, name, class, etc)
- Fixtures y Markers (para facilitar su ejecución y la selección de casos de prueba a correr). 

## Instrucciones de instalación de dependencias
- Descargar Python desde el sitio web: https://www.python.org/downloads/
- Luego en la terminal de VisualStudio, ejecutamos los siguientes comandos: 
pip install selenium (instala el framework de Selenium)
pip install pytest (instala la herramienta Pytest para ejecutar los casos de testing)
pip install pytest-html (instala la herramienta para generar reportes HTML)
pip install webdriver-manager (instala el webdriver para navegar por Chrome)

## Comando para ejecutar las pruebas (por ejemplo: pytest -v --html=reporte.html)
1) Para correr el script de preentrega (que incluye todo el flujo desde el Login hasta la verificación de producto en carrito): python3 preentrega.py

2) Para correr con Pytest todos los casos de prueba de la carpeta /test (Login, Verificar página y Agregar a carrito): pytest test/ -v

3) Para correr solo el script de "Login" con pytest utilizando el marker: pytest -m login

4) Para correr solo el script de "Verificar página" con pytest utilizando el marker: pytest -m verificar_pagina

5) Para correr solo el script de "Agregar carrito" con pytest utilizando el marker: pytest -m agregar_carrito

6) Para ejecutar el reporte HTML sobre los scripts en la carpeta /test: pytest test/ -v --html=reporte.html


