### **📌 Definición de Función en Python**
En **Python**, una función es un **bloque de código reutilizable** que se ejecuta cuando se le llama. Se define con la palabra clave `def`.

---

## **🔹 Sintaxis básica**
```python
def nombre_de_la_funcion(parametros):
    """Docstring opcional: describe la función"""
    # Código de la función
    return valor  # Opcional
```
✅ **`def`** → Define la función.  
✅ **`parametros`** → Datos que recibe la función (pueden ser opcionales).  
✅ **`return`** → Devuelve un resultado (puede omitirse).  
✅ **`"""Docstring"""`** → Descripción opcional de la función.

---

## **1️⃣ Ejemplo básico: Función sin parámetros**
```python
def saludar():
    print("¡Hola, bienvenido!")

saludar()  # Llamada a la función
```
**Salida:**
```
¡Hola, bienvenido!
```
✅ **Se define `saludar()` y se ejecuta con `saludar()`.**

---

## **2️⃣ Función con parámetros**
```python
def suma(a, b):
    return a + b

resultado = suma(3, 5)
print(resultado)  # 8
```
✅ **Recibe dos parámetros (`a` y `b`) y devuelve la suma.**

---

## **3️⃣ Parámetros con valores por defecto**
```python
def saludar(nombre="Invitado"):
    print(f"Hola, {nombre}!")

saludar()  # Hola, Invitado!
saludar("Carlos")  # Hola, Carlos!
```
✅ **Si no se pasa un argumento, usa el valor `"Invitado"` por defecto.**

---

## **4️⃣ Función con múltiples valores (`*args`)**
```python
def suma_todos(*numeros):
    return sum(numeros)

print(suma_todos(1, 2, 3, 4, 5))  # 15
```
✅ **`*args` permite pasar cualquier cantidad de argumentos.**

---

## **5️⃣ Función con parámetros clave (`**kwargs`)**
```python
def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Carlos", edad=30, ciudad="Madrid")
```
**Salida:**
```
nombre: Carlos
edad: 30
ciudad: Madrid
```
✅ **`**kwargs` permite recibir argumentos con nombre como un diccionario.**

---

## **6️⃣ Función lambda (anónima)**
```python
doble = lambda x: x * 2
print(doble(4))  # 8
```
✅ **Funciones rápidas en una línea.**

---

## **📌 Resumen**
| Tipo de función | Ejemplo |
|---------------|---------|
| **Sin parámetros** | `def saludar(): print("Hola")` |
| **Con parámetros** | `def suma(a, b): return a + b` |
| **Con valor por defecto** | `def saludar(nombre="Invitado")` |
| **Con `*args` (varios argumentos)** | `def suma_todos(*numeros): return sum(numeros)` |
| **Con `**kwargs` (argumentos clave-valor)** | `def mostrar_info(**datos): print(datos)` |
| **Lambda (función anónima)** | `doble = lambda x: x * 2` |
