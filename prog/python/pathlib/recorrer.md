### **📌 6️⃣ Recorrer directorios y listar archivos con `pathlib`**  
En esta sección aprenderemos cómo listar archivos y carpetas dentro de un directorio, tanto de manera sencilla como recursiva.

---

## **🔹 6.1 Listar archivos y carpetas en un directorio con `iterdir()`**  
El método `.iterdir()` devuelve un **iterador** con los archivos y carpetas dentro del directorio.

```python
from pathlib import Path

ruta = Path("mi_carpeta")

for elemento in ruta.iterdir():
    print(elemento)  # Muestra archivos y carpetas en 'mi_carpeta'
```
✅ **Devuelve rutas completas de archivos y carpetas.**  

---

## **🔹 6.2 Filtrar solo archivos o solo carpetas**  
Podemos usar `.is_file()` y `.is_dir()` para listar solo archivos o carpetas.

🔹 **Listar solo archivos**  
```python
for archivo in ruta.iterdir():
    if archivo.is_file():
        print(archivo)
```

🔹 **Listar solo carpetas**  
```python
for carpeta in ruta.iterdir():
    if carpeta.is_dir():
        print(carpeta)
```

✅ **Útil cuando queremos procesar solo archivos sin incluir carpetas.**

---

## **🔹 6.3 Buscar archivos con una extensión específica usando `glob()`**  
El método `.glob("*.extensión")` permite **buscar archivos con una extensión determinada**.

```python
for archivo in ruta.glob("*.txt"):
    print(archivo)  # Muestra solo archivos .txt
```
✅ **Filtra archivos por extensión.**  
✅ **No busca en subdirectorios (para eso, usa `rglob()`).**

---

## **🔹 6.4 Buscar archivos en subdirectorios con `rglob()`**  
El método `.rglob("*.extensión")` busca **archivos dentro de subdirectorios de forma recursiva**.

```python
for archivo in ruta.rglob("*.txt"):
    print(archivo)  # Muestra archivos .txt en todos los subdirectorios
```
✅ **Busca archivos en toda la estructura de carpetas.**  

📌 **Ejemplo: Buscar todos los archivos en la carpeta y subcarpetas:**  
```python
for archivo in ruta.rglob("*"):  # El "*" encuentra todos los archivos y carpetas
    print(archivo)
```
✅ **Lista todo el contenido de la carpeta y sus subcarpetas.**

---

## **🔹 6.5 Contar archivos en una carpeta**
Si necesitamos **contar cuántos archivos hay en un directorio**, podemos hacer esto:

```python
cantidad_archivos = len(list(ruta.glob("*")))
print(f"Total de archivos y carpetas: {cantidad_archivos}")
```

✅ **Devuelve el total de archivos y carpetas en el directorio.**

---

## **🔹 6.6 Buscar archivos por múltiples extensiones**  
Si queremos **buscar archivos con varias extensiones**, combinamos `glob()` con `itertools.chain()`.

```python
from itertools import chain

tipos = ["*.jpg", "*.png"]
archivos = chain(*(ruta.glob(ext) for ext in tipos))

for archivo in archivos:
    print(archivo)
```
✅ **Encuentra imágenes en formato `.jpg` y `.png`.**

---

## **📌 Resumen de la Sección 6**
| **Operación** | **Código** |
|--------------|------------|
| **Listar archivos y carpetas** | `ruta.iterdir()` |
| **Listar solo archivos** | `if archivo.is_file(): print(archivo)` |
| **Listar solo carpetas** | `if carpeta.is_dir(): print(carpeta)` |
| **Buscar archivos `.txt` en un directorio** | `ruta.glob("*.txt")` |
| **Buscar archivos `.txt` en subdirectorios** | `ruta.rglob("*.txt")` |
| **Buscar todos los archivos en subdirectorios** | `ruta.rglob("*")` |
| **Contar archivos en una carpeta** | `len(list(ruta.glob("*")))` |
| **Buscar múltiples tipos de archivos** | `chain(*(ruta.glob(ext) for ext in tipos))` |

