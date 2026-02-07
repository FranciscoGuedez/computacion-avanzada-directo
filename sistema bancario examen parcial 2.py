import json

class CuentaBancaria:
    def __init__(self, numero_cuenta, nombre_cliente, fecha_apertura="N/A", balance=0.0, historial=None):
        self.numero_cuenta = numero_cuenta
        self.nombre_cliente = nombre_cliente
        self.fecha_apertura = fecha_apertura
        self.balance = balance
        self.historial = historial if historial else []

    def registrar_transaccion(self, tipo, monto, descripcion=""):
        self.historial.append({
            "tipo": tipo,
            "monto": monto,
            "descripcion": descripcion,
            "balance": self.balance
        })

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
            self.registrar_transaccion("Depósito", monto)
            print(f"Depósito exitoso de $ {monto:.2f}. Nuevo balance: $ {self.balance:.2f}")
        else:
            print("El monto a depositar debe ser positivo.")

    def retirar(self, monto):
        if monto > 0:
            if monto <= self.balance:
                self.balance -= monto
                self.registrar_transaccion("Retiro", monto)
                print(f"Retiro exitoso de ${monto:.2f}. Nuevo balance: $ {self.balance:.2f}")
            else:
                print("Fondos insuficientes.")
        else:
            print("El monto a retirar debe ser positivo.")

    def pagar(self, monto, descripcion="Pago"):
        if monto > 0 and monto <= self.balance:
            self.balance -= monto
            self.registrar_transaccion("Pago", monto, descripcion)
            print(f"{descripcion} realizado por ${monto:.2f}. Nuevo balance: ${self.balance:.2f}")
        else:
            print("Fondos insuficientes o monto inválido.")

    def transferir(self, monto, cuenta_destino):
        if monto > 0 and monto <= self.balance:
            self.balance -= monto
            cuenta_destino.balance += monto
            self.registrar_transaccion("Transferencia enviada", monto, f"A {cuenta_destino.nombre_cliente}")
            cuenta_destino.registrar_transaccion("Transferencia recibida", monto, f"De {self.nombre_cliente}")
            print(f"Transferencia de ${monto:.2f} a {cuenta_destino.nombre_cliente} exitosa.")
            print(f"Tu nuevo balance: ${self.balance:.2f}")
        else:
            print("Fondos insuficientes o monto inválido.")

    def mostrar_informacion(self):
        print(f"\n--- Información de la cuenta ---")
        print(f"Cuenta: {self.numero_cuenta}")
        print(f"Cliente: {self.nombre_cliente}")
        print(f"Fecha de apertura: {self.fecha_apertura}")
        print(f"Balance actual: $ {self.balance:.2f}")

    def mostrar_historial(self):
        print("\n--- Historial de transacciones ---")
        if not self.historial:
            print("No hay transacciones registradas.")
        else:
            for t in self.historial:
                print(f"{t['tipo']} | $ {t['monto']:.2f} | {t['descripcion']} | Balance: ${t['balance']:.2f}")

    def to_dict(self):
        return {
            "numero_cuenta": self.numero_cuenta,
            "nombre_cliente": self.nombre_cliente,
            "fecha_apertura": self.fecha_apertura,
            "balance": self.balance,
            "historial": self.historial
        }


# ---------------- FUNCIONES PARA GUARDAR Y CARGAR ----------------
def guardar_cuentas(cuentas, archivo="cuentas.json"):
    data = {num: cuenta.to_dict() for num, cuenta in cuentas.items()}
    with open(archivo, "w") as f:
        json.dump(data, f, indent=4)

def cargar_cuentas(archivo="cuentas.json"):
    try:
        with open(archivo, "r") as f:
            data = json.load(f)
            return {num: CuentaBancaria(**info) for num, info in data.items()}
    except FileNotFoundError:
        return {}


# ---------------- MENÚ INTERACTIVO ----------------
def menu():
    cuentas = cargar_cuentas()

    # Si no hay cuentas guardadas, inicializamos con las predeterminadas
    if not cuentas:
        cuentas = {
            "30704762": CuentaBancaria("30704762", "Francisco Guedez", fecha_apertura="03/12/2025", balance=1000),
            "654321": CuentaBancaria("654321", "María Gómez", fecha_apertura="03/12/2025", balance=500)
        }

    while True:
        print("\n--- BIENVENIDO AL MENÚ BNC ---")
        print("1. Ingrese cuenta existente")
        print("2. Crear una nueva cuenta")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero = input("Ingrese su número de cuenta: ")
            if numero not in cuentas:
                print("Cuenta no encontrada.")
                continue
            cuenta_activa = cuentas[numero]

            while True:
                print("\n--- MENÚ BNC AHORROS NARANJA ---")
                print("1. Ver cuenta")
                print("2. Depositar")
                print("3. Retirar")
                print("4. Pagar")
                print("5. Transferir")
                print("6. Ver historial de transacciones")
                print("7. Cerrar sesión")

                opcion_cuenta = input("Seleccione una opción: ")

                if opcion_cuenta == "1":
                    cuenta_activa.mostrar_informacion()
                elif opcion_cuenta == "2":
                    monto = float(input("Ingrese monto a depositar: "))
                    cuenta_activa.depositar(monto)
                    guardar_cuentas(cuentas)
                elif opcion_cuenta == "3":
                    monto = float(input("Ingrese monto a retirar: "))
                    cuenta_activa.retirar(monto)
                    guardar_cuentas(cuentas)
                elif opcion_cuenta == "4":
                    monto = float(input("Ingrese monto del pago: "))
                    descripcion = input("Descripción del pago: ")
                    cuenta_activa.pagar(monto, descripcion)
                    guardar_cuentas(cuentas)
                elif opcion_cuenta == "5":
                    monto = float(input("Ingrese monto a transferir: "))
                    destino = input("Ingrese número de cuenta destino: ")
                    if destino in cuentas:
                        cuenta_activa.transferir(monto, cuentas[destino])
                        guardar_cuentas(cuentas)
                    else:
                        print("Cuenta destino no encontrada.")
                elif opcion_cuenta == "6":
                    cuenta_activa.mostrar_historial()
                elif opcion_cuenta == "7":
                    print("Sesión cerrada.")
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")

        elif opcion == "2":
            numero = input("Ingrese número de cuenta nuevo: ")
            if numero in cuentas:
                print("Ya existe una cuenta con ese número.")
            else:
                nombre = input("Ingrese nombre del cliente: ")
                fecha = input("Ingrese fecha de apertura (ejemplo 03/12/2025): ")
                balance = float(input("Ingrese balance inicial: "))
                cuentas[numero] = CuentaBancaria(numero, nombre, fecha, balance)
                guardar_cuentas(cuentas)
                print(f"Cuenta creada exitosamente para {nombre} con número {numero}.")

        elif opcion == "3":
            print("Gracias por usar el sistema BNC. ¡Hasta luego!")
            guardar_cuentas(cuentas)
            break
        else:
            print("Opción inválida. Intente de nuevo.")


# Ejecutar menú
menu()
