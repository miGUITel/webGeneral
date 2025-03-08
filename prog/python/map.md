### **📌 `map()` en Python**  
La función `map()` **aplica una función a cada elemento de un iterable** (lista, tupla, conjunto, etc.) y devuelve un **iterador** con los resultados.

**El map se declara pero no se ejecuta hasta que es necesario**: por ejemplo, cuado queremos imprimir la lista.

> mi ejemplo:
```py
temp1 = [33, 41]
def farenh(x):
    return 2 * x
temp2 = list(map(lambda x: x +11, temp1))
print(temp2)
```
---

## **🔹 Sintaxis básica**
```python
map(función, iterable)
```
- **`función`** → Se aplica a cada elemento del iterable.  
- **`iterable`** → Lista, tupla u otro objeto iterable cuyos elementos serán transformados.  

El resultado de `map()` es un **objeto iterable**, por lo que normalmente lo convertimos en `list()` o `tuple()` para ver los resultados.

---

## **1️⃣ Ejemplo simple: Elevar al cuadrado**
```python
numeros = [1, 2, 3, 4]

cuadrados = map(lambda x: x ** 2, numeros)
print(list(cuadrados))  # [1, 4, 9, 16]
```
✅ **Cada número de `numeros` es elevado al cuadrado.**

---

## **2️⃣ Usando `map()` con una función normal**
En lugar de `lambda`, puedes usar una función definida:

```python
def cuadrado(x):
    return x ** 2

numeros = [1, 2, 3, 4]
resultado = map(cuadrado, numeros)
print(list(resultado))  # [1, 4, 9, 16]
```

✅ **Más legible cuando la función es compleja.**

---

## **3️⃣ Transformar elementos de una lista**
```python
palabras = ["python", "java", "c++"]

mayusculas = map(str.upper, palabras)
print(list(mayusculas))  # ['PYTHON', 'JAVA', 'C++']
```
✅ **Convierte cada palabra a mayúsculas usando `str.upper`.**

---

## **4️⃣ Multiples iterables en `map()`**
Si pasamos varias listas, la función debe aceptar varios parámetros.

```python
numeros1 = [1, 2, 3]
numeros2 = [4, 5, 6]

suma = map(lambda x, y: x + y, numeros1, numeros2)
print(list(suma))  # [5, 7, 9]
```
✅ **Cada par de números se suma (`1+4`, `2+5`, `3+6`).**

---

## **5️⃣ Convertir valores (`int`, `str`, etc.)**
```python
numeros = ["1", "2", "3"]
enteros = map(int, numeros)
print(list(enteros))  # [1, 2, 3]
```
✅ **Convierte cada elemento de `str` a `int`.**

---

## **6️⃣ Filtrar `None` después de aplicar `map()`**
Si la función devuelve `None` para algunos valores, puedes combinar `map()` con `filter()`.

```python
def convertir(x):
    return int(x) if x.isdigit() else None

datos = ["10", "hola", "20"]
valores = map(convertir, datos)

# Eliminar los None
resultado = filter(lambda x: x is not None, valores)
print(list(resultado))  # [10, 20]
```
✅ **Solo se convierten los valores numéricos, ignorando los no válidos.**

---

## **📌 Comparación `map()` vs. List Comprehension**
### **🔹 `map()`**
```python
resultado = map(lambda x: x ** 2, numeros)
```
✔ Más eficiente en memoria (devuelve un iterador).  
❌ Menos intuitivo para operaciones simples.  

### **🔹 List Comprehension (Alternativa)**
```python
resultado = [x ** 2 for x in numeros]
```
✔ Más legible y más usado en Python moderno.  
❌ Puede ser menos eficiente si la lista es muy grande.  

---

## **📌 Resumen**
| Uso de `map()` | Ejemplo | Salida |
|---------------|---------|--------|
| **Elevar al cuadrado** | `map(lambda x: x**2, [1, 2, 3])` | `[1, 4, 9]` |
| **Convertir a mayúsculas** | `map(str.upper, ["hola", "mundo"])` | `['HOLA', 'MUNDO']` |
| **Sumar dos listas** | `map(lambda x, y: x + y, [1, 2], [3, 4])` | `[4, 6]` |
| **Convertir `str` a `int`** | `map(int, ["1", "2", "3"])` | `[1, 2, 3]` |

✔ **Usa `map()` cuando necesites aplicar una función a cada elemento de una lista sin crear una nueva lista de inmediato.**  
✔ **Para operaciones simples, `list comprehension` puede ser más claro.**  
