"""
Punto de entrada principal – Sistema Modular de Gestión de Usuarios.
Ejecutar con:  python main.py
"""

from app.config import configuracion
from app.usuarios import GestorUsuarios
from app.usuarios.validaciones import ErrorValidacion


# ──────────────────────────────────────────────
# Helpers de presentación
# ──────────────────────────────────────────────

def limpiar_pantalla() -> None:
    print("\n" + "=" * 55)


def cabecera() -> None:
    limpiar_pantalla()
    print(f"  {configuracion.app_name}  v{configuracion.app_version}")
    print(f"  Administrador: {configuracion.admin_user}")
    print("=" * 55)


def mostrar_menu() -> None:
    print("\n  [1] Registrar usuario")
    print("  [2] Listar usuarios")
    print("  [3] Buscar usuario por nombre")
    print("  [4] Buscar usuario por ID")
    print("  [5] Mostrar configuración")
    print("  [0] Salir")
    print()


def imprimir_usuario(u: dict) -> None:
    print(f"  ID: {u['id']}  │  {u['nombre']}  │  Edad: {u['edad']}  │  {u['email']}")


# ──────────────────────────────────────────────
# Acciones del menú
# ──────────────────────────────────────────────

def accion_registrar(gestor: GestorUsuarios) -> None:
    limpiar_pantalla()
    print("  REGISTRAR NUEVO USUARIO")
    print("-" * 55)
    try:
        nombre = input("  Nombre completo : ")
        edad   = input("  Edad            : ")
        email  = input("  Email           : ")

        usuario = gestor.registrar_usuario(nombre, edad, email)
        print(f"\n  ✔ Usuario registrado con éxito (ID: {usuario['id']})")
        print(f"    → {usuario['nombre']} | {usuario['edad']} años | {usuario['email']}")

    except (ErrorValidacion, ValueError) as e:
        print(f"\n  ✘ Error: {e}")


def accion_listar(gestor: GestorUsuarios) -> None:
    limpiar_pantalla()
    print("  LISTA DE USUARIOS")
    print("-" * 55)
    usuarios = gestor.listar_usuarios()

    if not usuarios:
        print("  No hay usuarios registrados.")
        return

    for u in usuarios:
        imprimir_usuario(u)

    print(f"\n  Total: {gestor.total_usuarios()} usuario(s).")


def accion_buscar_nombre(gestor: GestorUsuarios) -> None:
    limpiar_pantalla()
    print("  BUSCAR USUARIO POR NOMBRE")
    print("-" * 55)
    termino = input("  Ingrese nombre o fragmento: ")
    resultados = gestor.buscar_por_nombre(termino)

    if not resultados:
        print(f"\n  No se encontraron usuarios con '{termino}'.")
        return

    print(f"\n  Se encontraron {len(resultados)} resultado(s):")
    for u in resultados:
        imprimir_usuario(u)


def accion_buscar_id(gestor: GestorUsuarios) -> None:
    limpiar_pantalla()
    print("  BUSCAR USUARIO POR ID")
    print("-" * 55)
    try:
        uid = int(input("  Ingrese el ID del usuario: "))
        usuario = gestor.buscar_por_id(uid)

        if usuario:
            print("\n  Usuario encontrado:")
            imprimir_usuario(usuario)
        else:
            print(f"\n  No existe ningún usuario con ID {uid}.")

    except ValueError:
        print("\n  ✘ El ID debe ser un número entero.")


def accion_configuracion() -> None:
    limpiar_pantalla()
    print("  CONFIGURACIÓN DEL SISTEMA")
    print("-" * 55)
    print(configuracion)


# ──────────────────────────────────────────────
# Bucle principal
# ──────────────────────────────────────────────

def main() -> None:
    gestor = GestorUsuarios(admin_user=configuracion.admin_user)

    while True:
        cabecera()
        mostrar_menu()

        opcion = input("  Seleccione una opción: ").strip()

        if opcion == "1":
            accion_registrar(gestor)
        elif opcion == "2":
            accion_listar(gestor)
        elif opcion == "3":
            accion_buscar_nombre(gestor)
        elif opcion == "4":
            accion_buscar_id(gestor)
        elif opcion == "5":
            accion_configuracion()
        elif opcion == "0":
            print("\n  ¡Hasta luego!\n")
            break
        else:
            print("\n  ✘ Opción no válida. Intente de nuevo.")

        input("\n  Presione Enter para continuar...")


if __name__ == "__main__":
    main()
