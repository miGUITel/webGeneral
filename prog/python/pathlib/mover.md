### **📌 4️⃣ Mover y renombrar archivos y carpetas con `pathlib` y `shutil`**  
En esta sección veremos cómo **mover y renombrar archivos y directorios** con `pathlib` y, cuando sea necesario, `shutil`.

---

## **🔹 4.1 Renombrar un archivo con `rename()`**
El método `.rename()` permite cambiar el nombre de un archivo.

```python
from pathlib import Path

ruta_original = Path("archivo_viejo.txt")
ruta_nueva = Path("archivo_nuevo.txt")

if ruta_original.exists():
    ruta_original.rename(ruta_nueva)
    print("Archivo renombrado")
```
✅ **Si el archivo ya existe, lo sobrescribe sin advertencia**.

---

## **🔹 4.2 Mover un archivo a otro directorio con `rename()`**
```python
ruta_original = Path("archivo.txt")
ruta_destino = Path("nueva_carpeta/archivo.txt")

# Verifica si el destino existe
ruta_destino.parent.mkdir(parents=True, exist_ok=True)  # Crea la carpeta si no existe
ruta_original.rename(ruta_destino)
print("Archivo movido")
```
📌 **Notas**:
- `.rename()` funciona tanto para **mover como para renombrar archivos**.
- Si el **directorio de destino no existe**, debemos crearlo antes con `.mkdir(parents=True, exist_ok=True)`.
- **Si el archivo de destino ya existe, lo sobrescribe.**

---

## **🔹 4.3 Renombrar una carpeta**
El mismo método `.rename()` se usa para cambiar el nombre de una carpeta.

```python
ruta_original = Path("carpeta_vieja")
ruta_nueva = Path("carpeta_nueva")

if ruta_original.exists():
    ruta_original.rename(ruta_nueva)
    print("Carpeta renombrada")
```
✅ **Funciona igual que para archivos**.

---

## **🔹 4.4 Mover una carpeta a otra ubicación**
Si queremos **mover una carpeta completa**, usamos `.rename()`.

```python
ruta_original = Path("mi_carpeta")
ruta_destino = Path("nueva_ubicacion/mi_carpeta")

# Asegurar que el directorio de destino existe
ruta_destino.parent.mkdir(parents=True, exist_ok=True)
ruta_original.rename(ruta_destino)

print("Carpeta movida")
```
✅ **Mueve toda la carpeta con su contenido.**

---

## **🔹 4.5 Mover archivos y carpetas con `shutil.move()`**  
Si `.rename()` no funciona como esperas (por ejemplo, si intentas mover entre discos diferentes), usa `shutil.move()`.

```python
import shutil
from pathlib import Path

ruta_original = Path("archivo.txt")
ruta_destino = Path("otra_carpeta/archivo.txt")

shutil.move(str(ruta_original), str(ruta_destino))  # Mueve el archivo
print("Archivo movido con shutil")
```
✅ **`shutil.move()` funciona en cualquier sistema de archivos**, incluso si el destino está en otro disco.

📌 **Diferencias entre `rename()` y `shutil.move()`**:
| Método | ¿Mueve entre discos? | ¿Permite renombrar? | ¿Sobrescribe archivos? |
|--------|----------------------|----------------------|----------------------|
| `rename()` | ❌ No (solo en el mismo disco) | ✅ Sí | ✅ Sí |
| `shutil.move()` | ✅ Sí | ✅ Sí | ✅ Sí |

---

### **📌 Resumen de la Sección 4**
| **Operación** | **Código** |
|--------------|------------|
| **Renombrar un archivo** | `ruta_original.rename(ruta_nueva)` |
| **Mover un archivo a otra carpeta** | `ruta_original.rename(ruta_destino)` |
| **Renombrar una carpeta** | `ruta_original.rename(ruta_nueva)` |
| **Mover una carpeta a otra ubicación** | `ruta_original.rename(ruta_destino)` |
| **Mover archivos con `shutil`** | `shutil.move(str(origen), str(destino))` |

