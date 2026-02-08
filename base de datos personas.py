def mostrar_menu() -> None:
    print("\n___ Menú de Personas ___")
    print("1. Crear archivo personas.txt")
    print("2. Agregar persona")
    print("3. Leer lista de personas")
    print("0. Salir")

def pedir_cedula() -> str:
    while True:
        cedula = input("Ingrese la cédula (solo números): ")
        if cedula.isdigit():
            return cedula
        print("Cédula inválida. Solo se permiten números.\n")

def archivo_existe(nombre_archivo: str) -> bool:
    try:
        with open(nombre_archivo, "r"):
            return True
    except FileNotFoundError:
        return False

def main() -> None:
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        # OPCIÓN 1: Crear archivo con protección
        if opcion == "1":
            if archivo_existe("personas.txt"):
                print("\nEl archivo personas.txt YA existe.")
                decision = input("¿Deseas borrarlo y crear uno nuevo? (s/n): ")

                if decision.lower() == "s":
                    with open("personas.txt", "w") as archivo:
                        archivo.write("Base de datos de personas\n\n")
                    print("Archivo personas.txt fue REINICIADO.")
                else:
                    print("No se borró el archivo. Todo sigue igual.")
            else:
                with open("personas.txt", "w") as archivo:
                    archivo.write("Base de datos de personas\n\n")
                print("Archivo personas.txt creado por primera vez.")

        # OPCIÓN 2: Agregar persona
        elif opcion == "2":
            if not archivo_existe("personas.txt"):
                print("El archivo personas.txt no existe. Créalo primero con la opción 1.")
                continue

            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            cedula = pedir_cedula()

            with open("personas.txt", "a") as archivo:
                archivo.write(f"Nombre: {nombre}\n")
                archivo.write(f"Apellido: {apellido}\n")
                archivo.write(f"Cédula: {cedula}\n\n")

            print("Persona agregada correctamente.")

        # OPCIÓN 3: Leer archivo
        elif opcion == "3":
            if not archivo_existe("personas.txt"):
                print("El archivo personas.txt no existe. Créalo primero con la opción 1.")
                continue

            with open("personas.txt", "r") as archivo:
                contenido = archivo.read()
            print("\nLista de personas registradas:\n" + contenido)

        # SALIR
        elif opcion == "0":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
