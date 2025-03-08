### **📌 2️⃣ Trabajar con rutas en `pathlib.Path`**  
En esta sección aprenderemos cómo manejar rutas de archivos y directorios utilizando `pathlib.Path`.

---

## **🔹 2.1 Crear objetos `Path`**
En `pathlib`, una **ruta** se representa con la clase `Path`.  

📌 **Ejemplo: Crear una ruta relativa**  
```python
from pathlib import Path

ruta = Path("mi_archivo.txt")  # Ruta relativa al directorio actual
print(ruta)  # mi_archivo.txt
```

📌 **Ejemplo: Crear una ruta absoluta**  
```python
ruta = Path("/home/usuario/mi_archivo.txt")  # Linux/Mac
# ruta = Path("C:/Users/Usuario/mi_archivo.txt")  # Windows
print(ruta)  # Ruta completa
```
✅ `Path()` **convierte una cadena en un objeto de ruta**, permitiendo operaciones más intuitivas.

---

## **🔹 2.2 Obtener la ruta del directorio actual**
Puedes obtener la ruta **del directorio donde se ejecuta el script** con:
```python
ruta_actual = Path.cwd()
print(ruta_actual)  # /home/usuario/proyecto (Linux) o C:\Users\Usuario\proyecto (Windows)
```
✅ `Path.cwd()` devuelve el **directorio de trabajo actual**.

---

## **🔹 2.3 Obtener la ruta del script en ejecución**
Si necesitas la **ubicación del script que se está ejecutando**:
```python
ruta_script = Path(__file__).resolve()
print(ruta_script)  # /home/usuario/proyecto/script.py
```
✅ `Path(__file__).resolve()` obtiene la **ruta absoluta** del script.

---

## **🔹 2.4 Convertir una cadena a `Path`**
Si tienes una **ruta en formato de cadena (`str`)**, puedes convertirla a `Path` fácilmente:
```python
ruta_str = "/home/usuario/mi_archivo.txt"
ruta = Path(ruta_str)  # Convierte str en Path
print(ruta)  # /home/usuario/mi_archivo.txt
```

✅ `Path()` convierte rutas de **cadenas** en **objetos `Path`**, lo que facilita su manipulación.

---

## **🔹 2.5 Obtener información de archivos y directorios**
### **Obtener el nombre, extensión y carpeta de un archivo**
```python
ruta = Path("documentos/reporte.pdf")

print(ruta.name)     # reporte.pdf (nombre con extensión)
print(ruta.stem)     # reporte (solo el nombre, sin extensión)
print(ruta.suffix)   # .pdf (solo la extensión)
print(ruta.parent)   # documentos (directorio padre)
```

✅ `ruta.parent` devuelve **la carpeta donde está el archivo**.

---

## **🔹 2.6 Verificar si un archivo o directorio existe**
```python
ruta = Path("mi_archivo.txt")

if ruta.exists():
    print("El archivo o carpeta existe")
else:
    print("No existe")
```
✅ `ruta.exists()` verifica si la **ruta existe**.

---

## **🔹 2.7 Verificar si es un archivo o directorio**
```python
ruta = Path("mi_archivo.txt")

if ruta.is_file():
    print("Es un archivo")
elif ruta.is_dir():
    print("Es un directorio")
else:
    print("No es un archivo ni un directorio")
```
✅ **Diferencia entre `is_file()` y `is_dir()`:**
- `is_file()` → **True** si es un archivo.  
- `is_dir()` → **True** si es una carpeta.  

---

### **📌 Resumen de la Sección 2**
| **Operación** | **Código** |
|--------------|------------|
| Crear una ruta relativa | `Path("mi_archivo.txt")` |
| Crear una ruta absoluta | `Path("/home/usuario/mi_archivo.txt")` |
| Obtener el directorio actual | `Path.cwd()` |
| Obtener la ruta del script | `Path(__file__).resolve()` |
| Convertir `str` a `Path` | `Path("ruta_como_string")` |
| Nombre del archivo | `ruta.name` |
| Nombre sin extensión | `ruta.stem` |
| Extensión del archivo | `ruta.suffix` |
| Directorio padre | `ruta.parent` |
| Verificar si existe | `ruta.exists()` |
| Verificar si es archivo | `ruta.is_file()` |
| Verificar si es carpeta | `ruta.is_dir()` |

---
