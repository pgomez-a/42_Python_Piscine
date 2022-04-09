### ¿Qué es pip?
Pip es el gestor de paquetes estándar de Python. A grandes rasgos, es responsable de la intalación y gestión de todos aquellos paquetes que no forman parte de la librería estándar de Python. También se encarga de gestionar las dependencias de estos paquetes.

    pip install package_name             # Para instalar un paquete junto con sus dependencias
    pip uninstall package-name           # Para eliminar un paquete. No se eliminan las dependencias
    pip install -r requirements.txt      # Para instalar las dependencias especificadas en el archivo requirements.txt
    pip list                             # Para listar los paquetes instalados junto con su versión
    pip freeze                           # Para crear el archivo requirements.txt
    pip install --upgrade package_name   # Para actualizar un paquete
    pip check                            # Para comprobar que todos los paquetes instalados son compatibles
    pip show package_name                # Para obtener información sobre un paquete específico
    pip --help                           # Para obtener información relevante sobre el uso de pip

Cuando vamos a trabajar con un proyecto ya existente escrito en Python, es frecuente encontrarnos con un archivo "requirements.txt". Este archivo se utiliza para especificar los paquetes que se deben instalar para poder trabajar en el proyecto correctamente. De esta forma, cada línea del archivo indica el nombre de un paquete a instalar junto con la versión de dicho paquete.
