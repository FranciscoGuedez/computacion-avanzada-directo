# Base de Datos de Personas
  
Permite almacenar **nombre, apellido y cédula** en un archivo de texto (`personas.txt`) y mantener los datos de forma permanente.

El programa funciona mediante un menú interactivo que permite:

- Crear el archivo de base de datos  
- Agregar personas  
- Leer los registros guardados  
- Salir del sistema  

Todo esto sin usar módulos externos como `os`.

---

## Características principales

- **Menú interactivo** fácil de usar  
- **Validación de cédula** (solo números permitidos)  
- **Protección del archivo** para evitar borrar datos accidentalmente  
- **Formato legible** para cada persona registrada  
- **Almacenamiento persistente** en archivo `.txt`  
- **Compatible con cualquier sistema operativo**  

---

##  Estructura del archivo generado

Cada persona se guarda con el siguiente formato:

Nombre: Ana
Apellido: Torres
Cédula: 12345678


Con una línea en blanco entre cada registro para mayor claridad.

---

## ¿Cómo funciona?

###1. Crear archivo  
Si `personas.txt` ya existe, el programa pregunta si deseas borrarlo.  
Si no existe, lo crea automáticamente.

### 2. Agregar persona  
Solicita:

- Nombre  
- Apellido  
- Cédula (validada para que solo acepte números)

Luego guarda los datos en el archivo.

###  3. Leer registros  
Muestra todo el contenido del archivo en pantalla.  
Si el archivo no existe, el programa avisa al usuario.

###  4. Salir  
Finaliza el programa.