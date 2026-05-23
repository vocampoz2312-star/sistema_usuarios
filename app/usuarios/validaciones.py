"""
Módulo de validaciones para el sistema de usuarios.
Contiene funciones para validar datos de entrada del usuario.
"""


class ErrorValidacion(Exception):
    """Excepción personalizada para errores de validación."""
    pass


def validar_nombre(nombre: str) -> str:
    """
    Valida que el nombre no esté vacío y tenga formato correcto.

    Args:
        nombre: El nombre a validar.

    Returns:
        El nombre limpio (sin espacios extra).

    Raises:
        ErrorValidacion: Si el nombre es inválido.
    """
    nombre = nombre.strip()

    if not nombre:
        raise ErrorValidacion("El nombre no puede estar vacío.")

    if len(nombre) < 2:
        raise ErrorValidacion("El nombre debe tener al menos 2 caracteres.")

    if len(nombre) > 50:
        raise ErrorValidacion("El nombre no puede superar 50 caracteres.")

    if not all(c.isalpha() or c.isspace() for c in nombre):
        raise ErrorValidacion("El nombre solo puede contener letras y espacios.")

    return nombre.title()


def validar_edad(edad_str: str) -> int:
    """
    Valida que la edad sea un número entero positivo dentro de un rango razonable.

    Args:
        edad_str: La edad como cadena de texto.

    Returns:
        La edad como entero.

    Raises:
        ErrorValidacion: Si la edad es inválida.
    """
    try:
        edad = int(edad_str.strip())
    except ValueError:
        raise ErrorValidacion("La edad debe ser un número entero.")

    if edad < 0:
        raise ErrorValidacion("La edad no puede ser negativa.")

    if edad < 1:
        raise ErrorValidacion("La edad debe ser mayor a 0.")

    if edad > 120:
        raise ErrorValidacion("La edad ingresada no es válida (máximo 120).")

    return edad


def validar_email(email: str) -> str:
    """
    Valida que el email tenga un formato básico correcto.

    Args:
        email: El correo electrónico a validar.

    Returns:
        El email en minúsculas y sin espacios extra.

    Raises:
        ErrorValidacion: Si el email es inválido.
    """
    email = email.strip().lower()

    if not email:
        raise ErrorValidacion("El email no puede estar vacío.")

    if "@" not in email:
        raise ErrorValidacion("El email debe contener '@'.")

    partes = email.split("@")
    if len(partes) != 2 or not partes[0] or not partes[1]:
        raise ErrorValidacion("Formato de email inválido.")

    if "." not in partes[1]:
        raise ErrorValidacion("El dominio del email no es válido.")

    return email
