[VER Argumentos con PARSE](#argumentos-con-parse)

[Ejemplo de uso en Collatz.py](../python/pruebas/Collatz.py)

### 📌 **Manejo de Argumentos con `sys.argv` en Python**

El módulo `sys` permite acceder a los argumentos pasados al ejecutar un script desde la línea de comandos mediante `sys.argv`, que es una lista donde cada elemento representa un argumento.

---

### 🔹 **Significado de `sys.argv[i]`**
- `sys.argv[0]` → **Nombre del script** que se está ejecutando.
- `sys.argv[1]` → **Primer argumento** pasado al script.
- `sys.argv[2]` → **Segundo argumento**, y así sucesivamente.

📌 **Ejemplo de código (`argumentos.py`)**:
```python
import sys

print("Nombre del script:", sys.argv[0])

if len(sys.argv) > 1:
    print("Primer argumento:", sys.argv[1])

if len(sys.argv) > 2:
    print("Segundo argumento:", sys.argv[2])
```

📌 **Ejecutando el script en la terminal**:
```sh
python argumentos.py hola mundo
```
**Salida:**
```
Nombre del script: argumentos.py
Primer argumento: hola
Segundo argumento: mundo
```

---

### 🔹 **Cómo saber el número de argumentos**
El número de argumentos se obtiene con `len(sys.argv)`, que incluye el nombre del script.

📌 **Ejemplo para contar argumentos**:
```python
import sys

num_args = len(sys.argv) - 1  # Restamos 1 porque el primer elemento es el script
print(f"Número de argumentos recibidos: {num_args}")
```
**Ejecutando**:
```sh
python argumentos.py 10 20 30
```
**Salida:**
```
Número de argumentos recibidos: 3
```

📌 **Evitar errores al acceder a argumentos inexistentes**:
```python
if len(sys.argv) > 1:
    print(f"Primer argumento: {sys.argv[1]}")
else:
    print("No se proporcionaron argumentos.")
```

---

### 🔹 **Resumen**
| **Elemento** | **Significado** |
|-------------|----------------|
| `sys.argv[0]` | Nombre del script |
| `sys.argv[1]` | Primer argumento |
| `len(sys.argv)` | Número total de elementos (incluye el script) |

✅ **`sys.argv` es útil para recibir argumentos desde la terminal y automatizar scripts en Python.** 🚀

# Argumentos con Parse

### 📌 **Manejo de Argumentos con `argparse` en Python**  

El módulo `argparse` permite gestionar argumentos de línea de comandos de forma estructurada y con validación automática.

---

### 🔹 **Cómo funciona `argparse`**
- Define los argumentos que el script puede recibir.
- Permite asignar tipos (`int`, `float`, `str`).
- Genera automáticamente un mensaje de ayuda (`--help`).
- Facilita el uso de opciones (`-o`, `--opcion`).

---

### 🔹 **Ejemplo Básico**  
📌 **Script (`parse_example.py`)**:
```python
import argparse

parser = argparse.ArgumentParser(description="Ejemplo de argparse")

# Definir argumentos
parser.add_argument("nombre", help="Nombre de la persona")
parser.add_argument("-e", "--edad", type=int, help="Edad de la persona (opcional)")

# Procesar argumentos
args = parser.parse_args()

# Usar los valores ingresados
print(f"Hola, {args.nombre}!")
if args.edad:
    print(f"Tienes {args.edad} años.")
```

---

### 🔹 **Ejecutando el Script**
```sh
python parse_example.py Carlos -e 30
```
**Salida:**
```
Hola, Carlos!
Tienes 30 años.
```

Si ejecutamos `python parse_example.py --help`, se genera automáticamente un mensaje de ayuda:
```
usage: parse_example.py [-h] [-e EDAD] nombre

Ejemplo de argparse

positional arguments:
  nombre      Nombre de la persona

optional arguments:
  -h, --help  show this help message and exit
  -e EDAD, --edad EDAD  Edad de la persona (opcional)
```

---

### 🔹 **Resumen**
| **Característica** | **Ejemplo** |
|-------------------|------------|
| Argumento obligatorio | `parser.add_argument("nombre")` |
| Argumento opcional | `parser.add_argument("-e", "--edad", type=int)` |
| Obtener valores | `args.nombre`, `args.edad` |
| Ayuda automática | `python script.py --help` |

✅ **`argparse` es ideal para scripts más avanzados con múltiples opciones.** 🚀