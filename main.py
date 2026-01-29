import os

# Diccionario (tabla hash)
# clave: nombre del cliente
# valor: ruta del archivo
clientes = {}

CARPETA_CLIENTES = "clientes"

# Crear carpeta si no existe
if not os.path.exists(CARPETA_CLIENTES):
    os.makedirs(CARPETA_CLIENTES)


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


def menu():
    while True:
        print("\n--- Sistema Axanet ---")
        print("1. Crear nuevo cliente")
        print("2. Consultar cliente")
        print("3. Actualizar cliente")
        print("4. Borrar cliente")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_cliente()
        elif opcion == "2":
            consultar_cliente()
        elif opcion == "3":
            actualizar_cliente()
        elif opcion == "4":
            borrar_cliente()
        elif opcion == "5":
            print("👋 Saliendo del sistema")
            break
        else:
            print("⚠️ Opción no válida")


menu()
