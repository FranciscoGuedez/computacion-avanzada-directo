# Sistema Bancario en Python 

# Descripción General

 implementa un **sistema bancario interactivo** que permite:

- Crear cuentas bancarias  
- Iniciar sesión en cuentas existentes  
- Depositar, retirar, pagar y transferir dinero  
- Ver historial de transacciones  
- Guardar toda la información en un archivo JSON  
- Mantener los datos incluso después de cerrar el programa  

El sistema está construido con **Programación Orientada a Objetos (POO)** y utiliza **JSON** como base de datos ligera.

---

#  Estructura del Código

El programa se divide en tres partes principales:

1. **Clase `CuentaBancaria`**  
2. **Funciones para guardar y cargar datos (JSON)**  
3. **Menú interactivo principal y menú de cuenta**
---

#  Clase `CuentaBancaria`

La clase representa una cuenta bancaria individual.  
Cada cuenta tiene:

- Número de cuenta  
- Nombre del cliente  
- Fecha de apertura  
- Balance  
- Historial de transacciones  

---

## Constructor


def __init__(self, numero_cuenta, nombre_cliente, fecha_apertura="N/A", balance=0.0, historial=None):
    
# Atributos del Sistema Bancario en Python  


# Clase `CuentaBancaria` — Atributos

La clase `CuentaBancaria` contiene **5 atributos principales**.  
Estos atributos representan toda la información esencial de una cuenta bancaria.

---

## Lista de atributos

### 1. `numero_cuenta`
- **Tipo:** `str`
- **Descripción:**  
  Identificador único de la cuenta bancaria.  
  Es la clave principal para buscar, cargar y operar sobre una cuenta.

---

### 2. `nombre_cliente`
- **Tipo:** `str`
- **Descripción:**  
  Nombre completo del titular de la cuenta.  
  Se usa para mostrar información y registrar transacciones.

---

### 3. `fecha_apertura`
- **Tipo:** `str`
- **Valor por defecto:** `"N/A"`
- **Descripción:**  
  Fecha en la que se creó la cuenta.  
  Se almacena como texto para facilitar su lectura.

---

### 4. `balance`
- **Tipo:** `float`
- **Valor inicial:** `0.0` (si no se especifica)
- **Descripción:**  
  Cantidad de dinero disponible en la cuenta.  
  Este valor cambia con depósitos, retiros, pagos y transferencias.

---

### 5. `historial`
- **Tipo:** `list`
- **Valor inicial:** `[]` (lista vacía)
- **Descripción:**  
  Lista de transacciones realizadas por la cuenta.  
  Cada transacción es un diccionario con:
  - `tipo`
  - `monto`
  - `descripcion`
  - `balance` (después de la operación)

Ejemplo de una entrada del historial:

```json
{
  "tipo": "Depósito",
  "monto": 100.0,
  "descripcion": "",
  "balance": 1100.0
}

