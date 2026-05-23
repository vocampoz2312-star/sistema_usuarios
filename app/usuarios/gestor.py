"""
Módulo gestor de usuarios.
Contiene la clase GestorUsuarios con las operaciones CRUD principales.
"""

from .validaciones import validar_nombre, validar_edad, validar_email, ErrorValidacion


class GestorUsuarios:
    """
    Clase responsable de gestionar el registro, listado y búsqueda de usuarios.
    Almacena los usuarios en memoria (lista de diccionarios).
    """

    def __init__(self, admin_user: str = "admin"):
        """
        Inicializa el gestor con una lista vacía de usuarios.

        Args:
            admin_user: Nombre del usuario administrador del sistema.
        """
        self._usuarios: list[dict] = []
        self._admin_user = admin_user
        self._siguiente_id = 1

    # ------------------------------------------------------------------
    # Registro
    # ------------------------------------------------------------------

    def registrar_usuario(self, nombre: str, edad: str, email: str) -> dict:
        """
        Registra un nuevo usuario tras validar sus datos.

        Args:
            nombre: Nombre completo del usuario.
            edad:   Edad como cadena (se convierte a entero).
            email:  Correo electrónico del usuario.

        Returns:
            Diccionario con los datos del usuario registrado.

        Raises:
            ErrorValidacion: Si algún dato no supera la validación.
            ValueError: Si el email ya está registrado.
        """
        nombre_valido = validar_nombre(nombre)
        edad_valida   = validar_edad(edad)
        email_valido  = validar_email(email)

        # Verificar email duplicado
        if self._buscar_por_email(email_valido):
            raise ValueError(f"El email '{email_valido}' ya está registrado.")

        usuario = {
            "id":     self._siguiente_id,
            "nombre": nombre_valido,
            "edad":   edad_valida,
            "email":  email_valido,
        }
        self._usuarios.append(usuario)
        self._siguiente_id += 1
        return usuario

    # ------------------------------------------------------------------
    # Listado
    # ------------------------------------------------------------------

    def listar_usuarios(self) -> list[dict]:
        """
        Devuelve una copia de la lista completa de usuarios registrados.

        Returns:
            Lista de diccionarios con los datos de cada usuario.
        """
        return list(self._usuarios)

    def total_usuarios(self) -> int:
        """Retorna el número total de usuarios registrados."""
        return len(self._usuarios)

    # ------------------------------------------------------------------
    # Búsquedas
    # ------------------------------------------------------------------

    def buscar_por_nombre(self, nombre: str) -> list[dict]:
        """
        Busca usuarios cuyo nombre contenga la cadena indicada (sin distinguir mayúsculas).

        Args:
            nombre: Fragmento de nombre a buscar.

        Returns:
            Lista de usuarios que coinciden con la búsqueda.
        """
        termino = nombre.strip().lower()
        return [u for u in self._usuarios if termino in u["nombre"].lower()]

    def buscar_por_id(self, usuario_id: int) -> dict | None:
        """
        Busca un usuario por su identificador único.

        Args:
            usuario_id: ID del usuario.

        Returns:
            Diccionario del usuario o None si no existe.
        """
        for u in self._usuarios:
            if u["id"] == usuario_id:
                return u
        return None

    def _buscar_por_email(self, email: str) -> dict | None:
        """Método interno: busca un usuario por email exacto."""
        for u in self._usuarios:
            if u["email"] == email:
                return u
        return None

    # ------------------------------------------------------------------
    # Propiedades
    # ------------------------------------------------------------------

    @property
    def admin(self) -> str:
        """Retorna el nombre del usuario administrador."""
        return self._admin_user
