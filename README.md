## Propósito del proyecto
Este proyecto tiene como propósito la automatización de ciertas pruebas sobre funcionalidades esenciales del sitio www.saucedemo.com 
Estas pruebas consisten en la automatización del Login, la verificación de ciertos elementos de la página y agregar un producto al carrito, además de su corroboración. 
También contiene pruebas APIs a través de la paltaforma https://reqres.in/

## Tecnologías utilizadas
- Lenguaje Python
- Selenium (framework para automatización en navegadores)
- Pytest (para automatizar casos de testing)
- Pytest-html (para generar reportes)
- ChromeDriver /webdriver manager (para navegar por Chrome)
- Devtools (para la localización de selectores CSS para los elementos pertinentes, utilizando atributos y clases por ejemplo, ID, name, class, etc)
- Fixtures y Markers (para facilitar su ejecución y la selección de casos de prueba a correr). 
- POM (Page Objetc Model)
- Requests y APIs para verificar los códigos de resultados arrojados por los tests.

## Instrucciones de instalación de dependencias
- Descargar Python desde el sitio web: https://www.python.org/downloads/
- Luego en la terminal de VisualStudio, ejecutamos los siguientes comandos: 
pip install selenium (instala el framework de Selenium)
pip install pytest (instala la herramienta Pytest para ejecutar los casos de testing)
pip install pytest-html (instala la herramienta para generar reportes HTML)
pip install webdriver-manager (instala el webdriver para navegar por Chrome)
pip install requests (instala el feature para manejar APIs)

## Comando para ejecutar las pruebas (por ejemplo: pytest -v --html=reporte.html)
1) Para correr con Pytest todos los casos de prueba del proyecto final: pytest -v

2) Para correr los scripts con el marker "Login" con pytest: pytest -m login

3) Para correr los scripts con el marker "API" con pytest: pytest -m api

4) Para correr los scripts con el marker "Smoke" con pytest: pytest -m smoke

5) Para correr los scripts con el marker "Negativo" con pytest: pytest -m negativo

6) Para ejecutar el reporte HTML sobre los scripts: pytest -v --html=reporte.html

.......................

PROYECTO FINAL

1. Funcionalidades Específicas:
-Automatización de Casos de Prueba:
    Implementa al menos 5 casos de prueba para un sitio web demo (puede ser saucedemo.com, automationpractice.com, o cualquier otro sitio de práctica)
    Los casos de prueba deben cubrir flujos completos (ejemplo: login, navegación, búsqueda, añadir producto al carrito, checkout)
    Incluye al menos un escenario negativo (ejemplo: login con credenciales inválidas)

-Manejo de Datos de Prueba:
    Implementa alguna forma de parametrización para ejecutar las pruebas con diferentes conjuntos de datos
    Utiliza fuentes externas (archivos CSV, JSON, etc.) para leer los datos de prueba

-Implementación de Page Object Model:
    Crea clases para cada página que vayas a automatizar
    Implementa métodos que representen acciones en cada página
    Separa la lógica de las pruebas de la lógica de interacción con la página

-Gestión de Capturas de Pantalla:
    Implementa una funcionalidad que capture screenshots automáticamente cuando una prueba falla
    Almacena las capturas con nombres descriptivos que incluyan fecha/hora y nombre del test

2. Pruebas de API (Requests):
-Automatización de Endpoints:
    Implementa al menos 3 casos de prueba para una API pública (puede ser ReqRes, JSONPlaceholder, o cualquier otra API pública)
    Cubre diferentes métodos HTTP (GET, POST, DELETE)

-Validación de Respuestas:
    Verifica códigos de estado HTTP
    Valida estructura y contenido de las respuestas JSON
    Implementa assertions para diferentes escenarios (éxito, error, etc.)

-Encadenamiento de Peticiones (Opcional):
    Implementa un flujo donde una petición dependa del resultado de otra (ejemplo: crear un recurso y luego obtenerlo)

3. Generación de Reportes:
-Reportes HTML:
    Configura pytest para generar reportes HTML detallados
    Los reportes deben mostrar claramente los tests ejecutados, su estado (pasado/fallado) y duración
    Incluye capturas de pantalla en los reportes para las pruebas fallidas

-Logging:
    Implementa un sistema de logging que registre pasos clave durante la ejecución
    El log debe ser lo suficientemente detallado para facilitar la depuración

4. Integración con CI/CD:
-Github Actions
    Configura GitHub Actions para ejecutar tus pruebas automatizadas cuando se realice un push al repositorio
    Genera y almacena los reportes como artefactos de la ejecución

5. Control de Versiones y Documentación:
-Repositorio en GitHub:
    Sube el proyecto a un repositorio en GitHub
    Mantén un historial de commits que documente el progreso del proyecto
    Usa ramas para desarrollar funcionalidades y luego fusiónalas con la rama principal

-README.md:
    Incluye un archivo README.md que explique:
    El propósito del proyecto
    Las tecnologías utilizadas
    La estructura del proyecto
    ¿Cómo instalar las dependencias?
    ¿Cómo ejecutar las pruebas?
    ¿Cómo interpretar los reportes generados?