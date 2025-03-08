### **📌 Resumen de operaciones más importantes con `pathlib` y `shutil` en Python**  
Aquí tienes un **resumen estructurado** con las operaciones más utilizadas para **manejar rutas, archivos y directorios** en Python.

---

## **1️⃣ Trabajar con rutas (`pathlib.Path`)**
| **Operación** | **Código** |
|--------------|------------|
| **Crear una ruta relativa** | `ruta = Path("archivo.txt")` |
| **Crear una ruta absoluta** | `ruta = Path("/home/user/archivo.txt")` |
| **Obtener el directorio actual** | `Path.cwd()` |
| **Obtener la ruta del script en ejecución** | `Path(__file__).resolve()` |
| **Convertir `str` a `Path`** | `ruta = Path("ruta_como_string")` |
| **Nombre del archivo** | `ruta.name` |
| **Nombre sin extensión** | `ruta.stem` |
| **Extensión del archivo** | `ruta.suffix` |
| **Directorio padre** | `ruta.parent` |
| **Verificar si existe** | `ruta.exists()` |
| **Verificar si es archivo** | `ruta.is_file()` |
| **Verificar si es carpeta** | `ruta.is_dir()` |

---

## **2️⃣ Crear y eliminar archivos y carpetas**
| **Operación** | **Código** |
|--------------|------------|
| **Crear un archivo vacío** | `ruta.touch()` |
| **Escribir texto en un archivo** | `ruta.write_text("Texto")` |
| **Leer contenido de un archivo** | `ruta.read_text()` |
| **Eliminar un archivo** | `ruta.unlink()` |
| **Crear una carpeta** | `ruta.mkdir()` |
| **Crear una carpeta sin error si existe** | `ruta.mkdir(exist_ok=True)` |
| **Crear subdirectorios automáticamente** | `ruta.mkdir(parents=True, exist_ok=True)` |
| **Eliminar una carpeta vacía** | `ruta.rmdir()` |
| **Eliminar una carpeta con contenido** | `shutil.rmtree(ruta)` |

---

## **3️⃣ Mover y renombrar archivos y carpetas**
| **Operación** | **Código** |
|--------------|------------|
| **Renombrar un archivo** | `ruta.rename("nuevo_nombre.txt")` |
| **Mover un archivo a otra carpeta** | `ruta.rename("nueva_carpeta/archivo.txt")` |
| **Renombrar una carpeta** | `ruta.rename("carpeta_nueva")` |
| **Mover una carpeta a otra ubicación** | `ruta.rename("nueva_ubicacion/mi_carpeta")` |
| **Mover archivos con `shutil` (entre discos)** | `shutil.move(str(origen), str(destino))` |

---

## **4️⃣ Copiar archivos y carpetas (`shutil`)**
| **Operación** | **Código** |
|--------------|------------|
| **Copiar un archivo** | `shutil.copy(origen, destino)` |
| **Copiar un archivo con permisos** | `shutil.copy2(origen, destino)` |
| **Copiar una carpeta entera** | `shutil.copytree(origen, destino)` |
| **Copiar archivos con una extensión específica** | `shutil.copy(archivo, destino / archivo.name)` |
| **Copiar archivos sin copiar subcarpetas** | `if archivo.is_file(): shutil.copy(archivo, destino / archivo.name)` |
| **Copiar y cambiar el nombre del archivo** | `shutil.copy(origen, destino_con_nuevo_nombre)` |

---

## **5️⃣ Listar archivos y recorrer directorios**
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

---

## **6️⃣ Manejo de archivos y carpetas temporales (`tempfile`)**
| **Operación** | **Código** |
|--------------|------------|
| **Crear un archivo temporal** | `tempfile.NamedTemporaryFile()` |
| **Escribir en un archivo temporal** | `temp_file.write(b"texto")` |
| **Evitar que el archivo temporal se elimine** | `NamedTemporaryFile(delete=False)` |
| **Eliminar manualmente un archivo temporal** | `os.remove(temp_file.name)` |
| **Crear un directorio temporal** | `tempfile.TemporaryDirectory()` |
| **Ubicar archivos temporales en un directorio personalizado** | `NamedTemporaryFile(dir="ruta")` |

---

## **📌 Conclusión**
✔ **`pathlib` es la mejor opción para manejar rutas de archivos y directorios de forma intuitiva.**  
✔ **`shutil` complementa `pathlib` para copiar, mover y eliminar carpetas completas.**  
✔ **`tempfile` es ideal para archivos temporales que se eliminan automáticamente.**  
