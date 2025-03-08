### **📌 Generación de listas con `for` en Python (List Comprehension)**  
Las **listas por comprensión** (`list comprehension`) permiten generar **nuevas listas** a partir de otras listas o iterables de forma más **rápida y legible** que un `for` tradicional.

---

## **🔹 Sintaxis básica**
```python
nueva_lista = [expresión for elemento in lista_original]
```
- **`expresión`** → Operación que se aplicará a cada elemento.  
- **`elemento`** → Variable que representa cada valor de la lista original.  
- **`lista_original`** → Lista (o cualquier iterable) sobre la que iteramos.

---

## **🔹 Ejemplo simple: Duplicar valores**
```python
numeros = [1, 2, 3, 4]
dobles = [x * 2 for x in numeros]
print(dobles)  # [2, 4, 6, 8]
```
✅ **Cada elemento `x` se multiplica por 2 y se almacena en `dobles`.**

---

## **🔹 Con condicional (`if`)**
```python
numeros = [1, 2, 3, 4, 5, 6]
pares = [x for x in numeros if x % 2 == 0]
print(pares)  # [2, 4, 6]
```
✅ **Solo se incluyen los números pares (`if x % 2 == 0`).**

---

## **🔹 Con `if-else`**
```python
numeros = [1, 2, 3, 4]
resultado = ["par" if x % 2 == 0 else "impar" for x in numeros]
print(resultado)  # ['impar', 'par', 'impar', 'par']
```
✅ **Si el número es par, devuelve `"par"`, si no, `"impar"`.**

---

## **🔹 Anidando bucles (`for` dentro de `for`)**
```python
filas = [1, 2, 3]
columnas = ["A", "B"]

combinaciones = [(fila, columna) for fila in filas for columna in columnas]
print(combinaciones)  
# [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B'), (3, 'A'), (3, 'B')]
```
✅ **Crea combinaciones entre elementos de dos listas.**

---

## **📌 Resumen**
| **Expresión** | **Ejemplo** | **Salida** |
|--------------|------------|-----------|
| **Básico** | `[x * 2 for x in lista]` | `[2, 4, 6, 8]` |
| **Con `if`** | `[x for x in lista if x > 2]` | `[3, 4, 5]` |
| **Con `if-else`** | `["par" if x % 2 == 0 else "impar" for x in lista]` | `['impar', 'par']` |
| **Doble `for`** | `[(x, y) for x in lista1 for y in lista2]` | `[(1, 'A'), (1, 'B')]` |

✅ **Las comprensiones de listas son más eficientes y legibles que los `for` tradicionales.**  
