### **📌 1️⃣ Introducción a `pathlib` y `shutil` en Python**  
Esta sección explica qué son `pathlib` y `shutil`, sus ventajas y por qué se usan juntos para manipular rutas, archivos y directorios.

---

## **🔹 1.1 ¿Qué es `pathlib`?**  
`pathlib` es un **módulo moderno de Python** (desde Python 3.4) que **maneja rutas de archivos y directorios de manera más limpia y eficiente** que `os.path`.

📌 **Ventajas de `pathlib` sobre `os.path`**:
✔ Es **más intuitivo** y fácil de leer.  
✔ Soporta **operaciones de ruta de manera orientada a objetos**.  
✔ Compatible con **Windows, Linux y Mac** sin necesidad de usar `os.path.join()`.  

📌 **Ejemplo con `pathlib` vs. `os.path`**
```python
from pathlib import Path
import os

ruta_pathlib = Path("mi_archivo.txt")  # path estilo orientado a objetos
ruta_os = os.path.join("mi_archivo.txt")  # forma tradicional con os.path
```

---

## **🔹 1.2 ¿Qué es `shutil` y por qué se usa junto con `pathlib`?**  
`shutil` es un módulo que extiende `os` y permite realizar **operaciones avanzadas** como copiar y mover archivos o carpetas.

📌 **¿Por qué usar `shutil` junto con `pathlib`?**  
`pathlib` **no tiene métodos para copiar archivos ni directorios**, por lo que **necesitamos `shutil` para completar esas operaciones**.

✔ **`pathlib`** → Se usa para manejar **rutas, eliminar y mover archivos**.  
✔ **`shutil`** → Se usa para **copiar archivos o carpetas completas**.  

📌 **Ejemplo combinando `pathlib` y `shutil`**
```python
from pathlib import Path
import shutil

ruta_original = Path("archivo.txt")
ruta_copia = Path("copia_archivo.txt")

shutil.copy(ruta_original, ruta_copia)  # Copia el archivo usando shutil
```

---

## **🔹 1.3 Comparación: `pathlib` vs. `os.path`**
| Operación | `pathlib` ✅ (Recomendada) | `os.path` ❌ (Antiguo) |
|-----------|-----------------|------------------|
| Crear una ruta | `Path("archivo.txt")` | `os.path.join("archivo.txt")` |
| Obtener nombre de archivo | `ruta.name` | `os.path.basename(ruta)` |
| Obtener extensión | `ruta.suffix` | `os.path.splitext(ruta)[1]` |
| Verificar si existe | `ruta.exists()` | `os.path.exists(ruta)` |
| Crear carpeta | `ruta.mkdir()` | `os.mkdir(ruta)` |
| Eliminar archivo | `ruta.unlink()` | `os.remove(ruta)` |
| Mover archivo | `ruta.rename(nueva_ruta)` | `os.rename(ruta, nueva_ruta)` |
| **Copiar archivo** | ❌ No soportado | ✅ `shutil.copy()` |

💡 **Conclusión**: `pathlib` es **más limpio y legible**, pero **necesita `shutil` para copiar archivos**.

---

## **🔹 1.4 Instalación y compatibilidad**  
📌 `pathlib` y `shutil` vienen **incluidos en Python** por defecto, por lo que **no es necesario instalarlos**.

Verifica tu versión de Python:
```sh
python --version
```
✅ **Python 3.4+** → Puedes usar `pathlib`.  
✅ **Python 3.0+** → Puedes usar `shutil`.  

Si usas **Python 2.x**, no tienes `pathlib` y deberías actualizar a Python 3.

---

### 🚀 **¿Continuamos con la sección 2 (Trabajar con rutas en `pathlib`)?**