import json

def guardar_json(nombre_archivo, dato):
    try:
        with open(nombre_archivo, "r") as f:
            lista = json.load(f)
    except FileNotFoundError:
        lista = []

    lista.append(dato)

    with open(nombre_archivo, "w") as f:
        json.dump(lista, f, indent=4)

def ingresar_datos():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    cedula = input("Ingrese la cédula: ")

    guardar_json("nombres.json", nombre)
    guardar_json("apellidos.json", apellido)
    guardar_json("cedulas.json", cedula)

    print("\nDatos guardados correctamente en archivos JSON separados.")

ingresar_datos()
