# VERSION CON DEFECTOS, NO FUNCIONAL

import os

# Diccionario (tabla hash)
# clave: nombre del cliente
# valor: ruta del archivo
clientes = {}

CARPETA_CLIENTES = "clientes"
CARPETA_SOLICITUDES = "solicitudes"


# -----------
# Inicializacion
# -----------
def crear_carpetas():
    # Crear carpeta si no existe
    if not os.path.exists(CARPETA_CLIENTES):
        os.makedirs(CARPETA_CLIENTES)

    # Rellenar el diccionario si existen archivos

    for archivo in os.listdir(CARPETA_CLIENTES):
        if archivo.endswith(".txt"):
            nombre = archivo.replace(".txt", "").replace("_", " ")
            clientes[nombre] = f"{CARPETA_CLIENTES}/{archivo}"

    if not os.path.exists(CARPETA_SOLICITUDES):
        os.makedirs(CARPETA_SOLICITUDES)


ARCHIVO_CONTADOR = f"{CARPETA_SOLICITUDES}/contador.txt"


# -----------
# Funciones del cliente
# -----------


def crear_cliente():
    nombre = input("Nombre del cliente: ")

    if nombre in clientes:
        print("⚠️ El cliente ya existe.")
        return

    servicio = input("Servicio solicitado: ")
    archivo = f"{CARPETA_CLIENTES}/{nombre.replace(' ', '_')}.txt"

    with open(archivo, "w") as f:
        f.write(f"Cliente: {nombre}\n")
        f.write(f"Servicio: {servicio}\n")

    clientes[nombre] = archivo
    print("✅ Cliente creado correctamente.")


def consultar_cliente():
    nombre = input("Nombre del cliente: ")

    if nombre not in clientes:
        print("❌ Cliente no encontrado.")
        return

    with open(clientes[nombre], "r") as f:
        print("\n--- Información del cliente ---")
        print(f.read())


def actualizar_cliente():
    nombre = input("Nombre del cliente: ")

    if nombre not in clientes:
        print("❌ Cliente no encontrado.")
        return

    nuevo_servicio = input("Nuevo servicio solicitado: ")

    with open(clientes[nombre], "a") as f:
        f.write(f"Servicio adicional: {nuevo_servicio}\n")

    print("🔄 Cliente actualizado correctamente.")


def borrar_cliente():
    nombre = input("Nombre del cliente: ")

    if nombre not in clientes:
        print("❌ Cliente no encontrado.")
        return

    os.remove(clientes[nombre])
    del clientes[nombre]

    print("🗑️ Cliente eliminado correctamente.")


def listar_cliente():
    archivos = os.listdir(CARPETA_CLIENTES)

    # Filtrar solo archivos .txt (clientes)
    cliente = [c for c in archivos if c.endswith(".txt")]

    if not cliente:
        print("No hay clientes registrados")
        return

    print("\n📁 CLIENTES:")
    for c in cliente:
        print(" - ", c.replace(".txt", ""))


# ----------
# SOLICITUDES
# ----------


def registrar_solicitud():
    nombre = input("Nombre del solicitante: ")
    detalles = input("Descripcion de la solicitud: ")
    numero = obtener_siguiente_numero()

    archivo = f"{CARPETA_SOLICITUDES}/solicitud{numero}.txt"

    with open(archivo, "w", encoding="utf-8") as f:
        f.write(f"Solicitud #{numero}\n")
        f.write(f"Nombre del solicitante: {nombre}\n")
        f.write(f"Detalles: {detalles}\n")

    print("Solicitud registrada con éxito")


def obtener_siguiente_numero():
    # Si no existe el archivo, lo inicializamos en 0
    if not os.path.exists(ARCHIVO_CONTADOR):
        with open(ARCHIVO_CONTADOR, "w") as f:
            f.write("0")

    # Leer el número actual
    with open(ARCHIVO_CONTADOR, "r") as f:
        numero = int(f.read().strip())

    # Incrementar
    numero += 1

    # Guardar el nuevo número
    with open(ARCHIVO_CONTADOR, "w") as f:
        f.write(str(numero))

    return numero


def listar_solicitudes():
    archivos = os.listdir(CARPETA_SOLICITUDES)

    # Filtrar: solo mostrar archivos que empiecen con "solicitud"
    solicitudes = [a for a in archivos if a.startswith("solicitud")]

    if not solicitudes:
        print("No hay solicitudes registradas.\n")
        return

    print("\n📁 SOLICITUDES:")
    for s in solicitudes:
        print(" -", s.replace(".txt", ""))
    print()


def menu():
    while True:
        print("\n--- Sistema Axanet ---")
        print("1. Crear nuevo cliente")
        #print("2. Consultar cliente")
        #print("3. Actualizar cliente")
        print("4. Listar clientes")
        print("5. Borrar cliente")
        print("6. Registrar solicitud")
        print("7. Listar solicitudes")
        print("8. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_cliente()
        #elif opcion == "2":
        #    consultar_cliente()
        #elif opcion == "3":
        #    actualizar_cliente()
        elif opcion == "4":
            listar_cliente()
        elif opcion == "5":
            borrar_cliente()
        elif opcion == "6":
            registrar_solicitud()
        elif opcion == "7":
            listar_solicitudes()
        elif opcion == "8":
            print("👋 Saliendo del sistema")
            break
        else:
            print("⚠️ Opción no válida")


crear_carpetas()
menu()
