### **📌 3️⃣ Crear y eliminar archivos y carpetas con `pathlib` y `shutil`**  
En esta sección aprenderemos a **crear y eliminar archivos y directorios** utilizando `pathlib` y `shutil` cuando sea necesario.

---

## **🔹 3.1 Crear archivos con `pathlib.touch()`**  
El método `touch()` crea un archivo vacío si no existe.

```python
from pathlib import Path

ruta = Path("nuevo_archivo.txt")
ruta.touch()  # Crea el archivo
print("Archivo creado:", ruta.exists())  # True si se creó correctamente
```

📌 **Notas**:
- Si el archivo ya existe, `touch()` **no lo sobrescribe**.
- Es equivalente a `open("archivo.txt", "a").close()` en `os`.

---

## **🔹 3.2 Escribir en un archivo**
Puedes escribir directamente usando `.write_text()` (para texto) o `.write_bytes()` (para datos binarios).

```python
ruta = Path("archivo.txt")
ruta.write_text("Hola, este es un archivo de prueba.")  # Escribe texto en el archivo
```

✅ **Sobrescribe el archivo si ya existe.**  

🔹 **Leer contenido del archivo:**
```python
contenido = ruta.read_text()
print(contenido)  # Hola, este es un archivo de prueba.
```

---

## **🔹 3.3 Eliminar archivos con `unlink()`**  
Para eliminar un archivo usamos `.unlink()`.

```python
ruta = Path("archivo.txt")

if ruta.exists():
    ruta.unlink()  # Elimina el archivo
    print("Archivo eliminado")
```

📌 **Notas**:
- **Si el archivo no existe, lanzará un error**.  
- Para evitar el error, verifica con `if ruta.exists()` antes de eliminarlo.

---

## **🔹 3.4 Crear directorios con `mkdir()`**  
Para crear carpetas usamos `.mkdir()`.

```python
ruta = Path("mi_carpeta")
ruta.mkdir()  # Crea la carpeta
```

📌 **Notas**:
- Si la carpeta ya existe, **dará un error**.  
- Para evitar el error, usa `exist_ok=True`:

```python
ruta.mkdir(exist_ok=True)  # No lanza error si la carpeta ya existe
```

🔹 **Crear subdirectorios automáticamente**  
Si necesitas crear varias carpetas a la vez:
```python
ruta = Path("padre/hijo/nieto")
ruta.mkdir(parents=True, exist_ok=True)
```
✅ **Crea todas las carpetas necesarias sin errores.**

---

## **🔹 3.5 Eliminar directorios**
### **Eliminar una carpeta vacía con `rmdir()`**
```python
ruta = Path("mi_carpeta")

if ruta.exists():
    ruta.rmdir()  # Elimina la carpeta si está vacía
    print("Carpeta eliminada")
```
📌 **Si la carpeta tiene archivos dentro, `rmdir()` dará error**.  

---

### **Eliminar una carpeta con contenido usando `shutil.rmtree()`**
Si la carpeta tiene archivos, `pathlib` no puede eliminarla directamente. **Usamos `shutil.rmtree()`**:

```python
import shutil

ruta = Path("carpeta_con_archivos")

if ruta.exists():
    shutil.rmtree(ruta)  # Elimina la carpeta y su contenido
    print("Carpeta y archivos eliminados")
```

✅ **`shutil.rmtree()` elimina carpetas con contenido.**  
⚠ **¡Usa esto con precaución, ya que borra todo sin preguntar!**

---

### **📌 Resumen de la Sección 3**
| **Operación** | **Código** |
|--------------|------------|
| **Crear un archivo vacío** | `ruta.touch()` |
| **Escribir texto en un archivo** | `ruta.write_text("Texto")` |
| **Leer un archivo** | `ruta.read_text()` |
| **Eliminar un archivo** | `ruta.unlink()` |
| **Crear una carpeta** | `ruta.mkdir()` |
| **Crear una carpeta sin error si existe** | `ruta.mkdir(exist_ok=True)` |
| **Crear subdirectorios automáticamente** | `ruta.mkdir(parents=True, exist_ok=True)` |
| **Eliminar una carpeta vacía** | `ruta.rmdir()` |
| **Eliminar una carpeta con contenido** | `shutil.rmtree(ruta)` |

