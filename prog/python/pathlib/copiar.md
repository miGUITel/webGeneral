### **📌 5️⃣ Copiar archivos y carpetas con `shutil` (complementando `pathlib`)**  
En esta sección aprenderemos a **copiar archivos y carpetas** usando `shutil`, ya que `pathlib` **no tiene funciones para copiar**.

---

## **🔹 5.1 Copiar un archivo con `shutil.copy()`**
El método `shutil.copy()` copia un archivo a otra ubicación.

```python
import shutil
from pathlib import Path

ruta_origen = Path("archivo.txt")
ruta_destino = Path("copia_archivo.txt")

shutil.copy(ruta_origen, ruta_destino)  # Copia el archivo
print("Archivo copiado")
```
✅ **Si el archivo de destino ya existe, se sobrescribe.**  
✅ **Mantiene el contenido, pero no los permisos originales.**

---

## **🔹 5.2 Copiar un archivo conservando permisos (`shutil.copy2()`)**
Si queremos copiar **manteniendo la fecha de creación y permisos**, usamos `copy2()`.

```python
shutil.copy2("archivo.txt", "copia_archivo.txt")
```
✅ **Diferencia entre `copy()` y `copy2()`**:
| Método | Copia contenido | Copia permisos | Copia metadatos (fecha de creación) |
|--------|---------------|---------------|-----------------|
| `shutil.copy()` | ✅ Sí | ❌ No | ❌ No |
| `shutil.copy2()` | ✅ Sí | ✅ Sí | ✅ Sí |

---

## **🔹 5.3 Copiar una carpeta con `shutil.copytree()`**
Para copiar **una carpeta entera con su contenido**, usamos `copytree()`.

```python
ruta_origen = Path("carpeta_original")
ruta_destino = Path("copia_carpeta")

shutil.copytree(ruta_origen, ruta_destino)
print("Carpeta copiada")
```
✅ **Copia todos los archivos y subdirectorios.**  
❌ **Si la carpeta de destino ya existe, lanzará un error.**  

🔹 **Para evitar errores, usa `dirs_exist_ok=True` (Python 3.8+):**
```python
shutil.copytree(ruta_origen, ruta_destino, dirs_exist_ok=True)
```
✅ **Sobrescribe archivos dentro de la carpeta destino sin eliminar la carpeta.**

---

## **🔹 5.4 Copiar archivos con extensión específica**
Podemos copiar **solo archivos con una determinada extensión**.

```python
ruta_origen = Path("carpeta_origen")
ruta_destino = Path("carpeta_destino")

# Asegurar que la carpeta destino existe
ruta_destino.mkdir(parents=True, exist_ok=True)

# Copiar solo archivos .txt
for archivo in ruta_origen.glob("*.txt"):
    shutil.copy(archivo, ruta_destino / archivo.name)

print("Archivos .txt copiados")
```
✅ **Solo copia archivos `.txt` y mantiene los nombres originales.**

---

## **🔹 5.5 Copiar archivos de una carpeta a otra (sin subcarpetas)**
```python
for archivo in ruta_origen.iterdir():
    if archivo.is_file():  # Verifica que sea un archivo (no una carpeta)
        shutil.copy(archivo, ruta_destino / archivo.name)
```
✅ **Evita copiar subcarpetas, solo copia archivos directamente dentro del directorio.**

---

## **🔹 5.6 Copiar archivos con nombres modificados**
Si queremos copiar un archivo y cambiar su nombre en el proceso:

```python
ruta_origen = Path("documento.pdf")
ruta_destino = Path("copias/nuevo_nombre.pdf")

ruta_destino.parent.mkdir(parents=True, exist_ok=True)  # Crear carpeta si no existe
shutil.copy(ruta_origen, ruta_destino)
```
✅ **El archivo copiado tendrá un nombre diferente en la carpeta destino.**

---

## **📌 Resumen de la Sección 5**
| **Operación** | **Código** |
|--------------|------------|
| **Copiar un archivo** | `shutil.copy(origen, destino)` |
| **Copiar un archivo con permisos** | `shutil.copy2(origen, destino)` |
| **Copiar una carpeta entera** | `shutil.copytree(origen, destino)` |
| **Copiar archivos con una extensión específica** | `shutil.copy(archivo, destino / archivo.name)` |
| **Copiar archivos sin copiar subcarpetas** | `if archivo.is_file(): shutil.copy(archivo, destino / archivo.name)` |
| **Copiar y cambiar el nombre del archivo** | `shutil.copy(origen, destino_con_nuevo_nombre)` |

