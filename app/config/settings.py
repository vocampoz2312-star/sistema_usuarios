"""
Módulo de configuración del sistema.
Lee las variables de entorno desde el archivo .env usando python-dotenv.
"""

import os
from pathlib import Path
from dotenv import load_dotenv


def _cargar_env() -> None:
    """Carga el archivo .env buscando desde la raíz del proyecto hacia arriba."""
    # Sube dos niveles desde app/config/ hasta la raíz del proyecto
    raiz = Path(__file__).resolve().parent.parent.parent
    archivo_env = raiz / ".env"

    if archivo_env.exists():
        load_dotenv(dotenv_path=archivo_env)
    else:
        # Fallback: busca .env en el directorio de trabajo actual
        load_dotenv()


# Cargar variables al importar el módulo
_cargar_env()


class Configuracion:
    """
    Clase que expone las variables de entorno como atributos tipados.
    Si una variable no existe, usa el valor por defecto definido aquí.
    """

    def __init__(self):
        self.app_name:    str = os.getenv("APP_NAME", "Sistema Usuarios")
        self.app_version: str = os.getenv("APP_VERSION", "1.0")
        self.admin_user:  str = os.getenv("ADMIN_USER", "admin")

    def __str__(self) -> str:
        return (
            f"[Configuración]\n"
            f"  Nombre:   {self.app_name}\n"
            f"  Versión:  {self.app_version}\n"
            f"  Admin:    {self.admin_user}"
        )


# Instancia global lista para importar
configuracion = Configuracion()
