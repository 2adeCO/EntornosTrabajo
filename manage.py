#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# Esta línea indica que el script debe ser ejecutado con el intérprete de Python del entorno (shebang)

import os  # Importa el módulo 'os' para interactuar con variables de entorno del sistema operativo
import sys  # Importa el módulo 'sys' para acceder a argumentos pasados desde la línea de comandos


def main():
    """Run administrative tasks."""
    # Establece una variable de entorno para que Django sepa cuál es el módulo de configuración (settings) a usar
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mundocoleccionables.settings')
    
    try:
        # Intenta importar la función que permite ejecutar comandos administrativos de Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Si Django no está instalado, lanza un error explicativo
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Ejecuta el comando recibido desde la línea de comandos (como 'runserver', 'migrate', etc.)
    execute_from_command_line(sys.argv)


# Este bloque asegura que la función 'main()' solo se ejecute si este archivo se ejecuta directamente
if __name__ == '__main__':
    main()
