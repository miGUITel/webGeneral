### **📌 7️⃣ Manejo de archivos temporales con `tempfile`**  
El módulo `tempfile` en Python permite crear archivos y directorios **temporales** que se eliminan automáticamente cuando ya no se necesitan.

---

## **🔹 7.1 Crear un archivo temporal con `NamedTemporaryFile()`**  
La función `NamedTemporaryFile()` crea un **archivo temporal con nombre**, que se elimina automáticamente al cerrarlo.

```python
import tempfile

with tempfile.NamedTemporaryFile(delete=True) as temp_file:
    print("Archivo temporal creado:", temp_file.name)
    temp_file.write(b"Datos temporales")  # Escribimos en el archivo
    temp_file.seek(0)  # Volver al inicio del archivo
    print("Contenido:", temp_file.read())  # Leer contenido
```
✅ **Se elimina automáticamente al salir del bloque `with`**.  
✅ **El archivo tiene un nombre accesible (`temp_file.name`)**.  
✅ **`write()` usa `b"..."` porque `NamedTemporaryFile()` maneja archivos binarios por defecto**.

---

## **🔹 7.2 Mantener un archivo temporal después de cerrarlo**
Por defecto, `NamedTemporaryFile()` elimina el archivo al cerrarlo.  
Si queremos mantenerlo, usamos `delete=False`:

```python
temp_file = tempfile.NamedTemporaryFile(delete=False)
print("Archivo temporal creado:", temp_file.name)

temp_file.write(b"Datos persistentes")
temp_file.close()  # Debemos cerrarlo manualmente
```
✅ **El archivo no se elimina automáticamente** y se puede acceder después de cerrar.

📌 **Para eliminarlo manualmente**:
```python
import os
os.remove(temp_file.name)
print("Archivo temporal eliminado")
```

---

## **🔹 7.3 Crear un directorio temporal con `TemporaryDirectory()`**  
Si necesitamos un **directorio temporal**, usamos `TemporaryDirectory()`:

```python
with tempfile.TemporaryDirectory() as temp_dir:
    print("Directorio temporal creado:", temp_dir)

    ruta_temp = Path(temp_dir) / "archivo.txt"
    ruta_temp.write_text("Contenido de prueba")

    print("Archivo creado en el directorio temporal:", ruta_temp)
```
✅ **La carpeta se elimina automáticamente al salir del bloque `with`**.  
✅ **Podemos crear archivos dentro del directorio temporal**.

---

## **🔹 7.4 Personalizar la ubicación del archivo temporal**
Por defecto, los archivos temporales se crean en el directorio del sistema (`/tmp/` en Linux o `%TEMP%` en Windows).  
Podemos especificar otra ubicación:

```python
temp_file = tempfile.NamedTemporaryFile(dir="mi_directorio_temporal", delete=False)
print("Archivo temporal en ruta personalizada:", temp_file.name)
```
✅ **Crea el archivo temporal en una carpeta personalizada**.

---

## **📌 Resumen de la Sección 7**
| **Operación** | **Código** |
|--------------|------------|
| **Crear un archivo temporal** | `tempfile.NamedTemporaryFile()` |
| **Escribir en un archivo temporal** | `temp_file.write(b"texto")` |
| **Evitar que el archivo temporal se elimine** | `NamedTemporaryFile(delete=False)` |
| **Eliminar manualmente un archivo temporal** | `os.remove(temp_file.name)` |
| **Crear un directorio temporal** | `tempfile.TemporaryDirectory()` |
| **Ubicar archivos temporales en un directorio personalizado** | `NamedTemporaryFile(dir="ruta")` |

