# ------------------------------
# Algoritmo para realizar una compra usando un método de pago
# ------------------------------

productos = {
    1: {"nombre": "Camisa", "precio": 15.00},
    2: {"nombre": "Pantalón", "precio": 25.00},
    3: {"nombre": "Zapatos", "precio": 40.00}
}

def mostrar_productos():
    print("\n--- PRODUCTOS DISPONIBLES ---")
    for id, info in productos.items():
        print(f"{id}. {info['nombre']} - $ {info['precio']:.2f}")

def seleccionar_producto():
    while True:
        try:
            opcion = int(input("Seleccione un producto: "))
            if opcion in productos:
                return productos[opcion]
            else:
                print("Producto inválido.")
        except ValueError:
            print("Ingrese un número válido.")

def seleccionar_metodo_pago():
    print("\n--- MÉTODOS DE PAGO ---")
    print("1. Tarjeta de débito")
    print("2. Tarjeta de crédito")
    print("3. Pago móvil")
    print("4. Transferencia bancaria")
    print("5. Efectivo")

    while True:
        metodo = input("Seleccione un método de pago: ")
        if metodo in ["1", "2", "3", "4", "5"]:
            return metodo
        else:
            print("Método inválido.")

def validar_pago(metodo, total):
    print("\nProcesando pago...")

    if metodo == "5":  # Efectivo
        efectivo = float(input("Ingrese el monto entregado: "))
        if efectivo >= total:
            cambio = efectivo - total
            print(f"Pago exitoso. Su cambio es: $ {cambio:.2f}")
            return True
        else:
            print("Monto insuficiente.")
            return False

    # Métodos electrónicos (simulación)
    print("Pago aprobado electrónicamente.")
    return True

def realizar_compra():
    mostrar_productos()
    producto = seleccionar_producto()

    cantidad = int(input("Ingrese la cantidad: "))
    total = producto["precio"] * cantidad

    print(f"\nTotal a pagar: $ {total:.2f}")

    metodo = seleccionar_metodo_pago()

    if validar_pago(metodo, total):
        print("\nCompra realizada con éxito.")
        print(f"Producto: {producto['nombre']}")
        print(f"Cantidad: {cantidad}")
        print(f"Total pagado: $ {total:.2f}")
    else:
        print("\nLa compra no pudo completarse.")

# Ejecutar algoritmo
realizar_compra()
