### **📌 Tipos de datos complejos más utilizados en Python**
Python tiene varios tipos de datos complejos que permiten almacenar y manipular colecciones de elementos. Aquí tienes los más utilizados:

| Tipo de dato | Descripción |
|-------------|-------------|
| **`list` (Lista)** | Colección ordenada y **mutable** que permite almacenar elementos de distintos tipos. Se define con `[]`. |
| **`tuple` (Tupla)** | Colección ordenada e **inmutable**, lo que significa que no se puede modificar después de su creación. Se define con `()`. |
| **`set` (Conjunto)** | Colección **desordenada y sin elementos duplicados**, útil para operaciones de conjuntos. Se define con `{}`. |
| **`frozenset`** | Variante inmutable de `set`, no se pueden agregar ni eliminar elementos una vez creado. |
| **`dict` (Diccionario)** | Estructura de pares **clave-valor**, donde las claves son únicas. Se define con `{clave: valor}`. |
| **`deque` (Cola doblemente terminada)** | Similar a `list`, pero más eficiente para operaciones de inserción y eliminación en ambos extremos. Se encuentra en `collections`. |
| **`Counter` (Contador)** | Diccionario especializado en contar la frecuencia de elementos en una colección. Se encuentra en `collections`. |
| **`defaultdict`** | Similar a `dict`, pero asigna un valor por defecto si la clave no existe. Se encuentra en `collections`. |
| **`OrderedDict`** | Diccionario que mantiene el orden de inserción de los elementos. (Python 3.7+ usa `dict` con la misma funcionalidad). |

---
### **📌 Tipos de datos complejos en Python con descripción y ejemplos**  
Aquí tienes una explicación más detallada de cada tipo de dato complejo en Python, junto con un ejemplo práctico.

---

## **1️⃣ `list` (Lista)**
✔ **Colección ordenada y mutable** que permite almacenar elementos de diferentes tipos.  
✔ Soporta **índices negativos, slicing y métodos como `append()`, `remove()` y `sort()`**.  

🔹 **Ejemplo de uso:**
```python
frutas = ["manzana", "banana", "cereza"]
frutas.append("naranja")  # Agrega un elemento
print(frutas)  # ['manzana', 'banana', 'cereza', 'naranja']
```

---

## **2️⃣ `tuple` (Tupla)**
✔ **Colección ordenada e inmutable**.  
✔ Al no poder modificarse, son más eficientes en términos de rendimiento.  
✔ Se utilizan cuando los datos **no deben cambiar**.  

🔹 **Ejemplo de uso:**
```python
coordenadas = (10, 20)
print(coordenadas[0])  # 10

# Error si intentamos modificarla:
# coordenadas[0] = 30  # ❌ TypeError: 'tuple' object does not support item assignment
```

---

## **3️⃣ `set` (Conjunto)**
✔ **Colección desordenada y sin duplicados**.  
✔ Soporta operaciones como **unión, intersección y diferencia**.  
✔ Útil cuando **necesitamos almacenar elementos únicos**.  

🔹 **Ejemplo de uso:**
```python
numeros = {1, 2, 3, 4, 4, 5}  # Duplicados se eliminan automáticamente
numeros.add(6)  
print(numeros)  # {1, 2, 3, 4, 5, 6}
```

---

## **4️⃣ `frozenset` (Conjunto inmutable)**
✔ Similar a `set`, pero **inmutable** (no se pueden agregar ni eliminar elementos).  
✔ Se usa cuando necesitamos **conjuntos inmutables como claves en un diccionario**.  

🔹 **Ejemplo de uso:**
```python
fs = frozenset([1, 2, 3, 4])
# fs.add(5)  # ❌ AttributeError: 'frozenset' object has no attribute 'add'
print(fs)  # frozenset({1, 2, 3, 4})
```

---

## **5️⃣ `dict` (Diccionario)**
✔ **Estructura clave-valor** donde cada clave debe ser única.  
✔ Se accede a los valores mediante sus claves en lugar de índices.  
✔ Desde **Python 3.7+**, los diccionarios mantienen el orden de inserción.  

🔹 **Ejemplo de uso:**
```python
persona = {"nombre": "Carlos", "edad": 30, "ciudad": "Madrid"}
print(persona["nombre"])  # "Carlos"

# Modificar valor
persona["edad"] = 31  
print(persona)  # {'nombre': 'Carlos', 'edad': 31, 'ciudad': 'Madrid'}
```

---

## **6️⃣ `deque` (Cola doblemente terminada)**
✔ **Más eficiente que `list` para inserciones y eliminaciones en ambos extremos**.  
✔ Se encuentra en el módulo `collections`.  

🔹 **Ejemplo de uso:**
```python
from collections import deque

cola = deque(["Ana", "Pedro", "Luis"])
cola.append("Sofía")  # Agrega al final
cola.appendleft("Carlos")  # Agrega al inicio
print(cola)  # deque(['Carlos', 'Ana', 'Pedro', 'Luis', 'Sofía'])

cola.pop()  # Elimina el último
cola.popleft()  # Elimina el primero
print(cola)  # deque(['Ana', 'Pedro', 'Luis'])
```

---

## **7️⃣ `Counter` (Contador)**
✔ **Cuenta la frecuencia de elementos en una lista o cadena**.  
✔ Se encuentra en `collections`.  

🔹 **Ejemplo de uso:**
```python
from collections import Counter

letras = "banana"
conteo = Counter(letras)
print(conteo)  # Counter({'a': 3, 'n': 2, 'b': 1})
```

---

## **8️⃣ `defaultdict` (Diccionario con valores por defecto)**
✔ **Evita errores al acceder a claves inexistentes**, asignando un valor por defecto.  
✔ Se encuentra en `collections`.  

🔹 **Ejemplo de uso:**
```python
from collections import defaultdict

diccionario = defaultdict(int)  # Valor por defecto: 0
diccionario["a"] += 1  # No da error si la clave no existe
print(diccionario)  # {'a': 1}
```

---

## **9️⃣ `OrderedDict` (Diccionario ordenado)**
✔ Similar a `dict`, pero **mantiene el orden de inserción en versiones anteriores a Python 3.7**.  
✔ En **Python 3.7+**, los `dict` normales ya mantienen el orden de inserción.  

🔹 **Ejemplo de uso:**
```python
from collections import OrderedDict

ordenado = OrderedDict()
ordenado["a"] = 1
ordenado["b"] = 2
ordenado["c"] = 3
print(ordenado)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])
```

---

## **📌 Resumen**
| Tipo de dato | Características principales | Mutable |
|-------------|----------------------|---------|
| `list` | Ordenado, permite duplicados, mutable | ✅ Sí |
| `tuple` | Ordenado, permite duplicados, inmutable | ❌ No |
| `set` | No ordenado, sin duplicados | ✅ Sí |
| `frozenset` | No ordenado, sin duplicados, inmutable | ❌ No |
| `dict` | Clave-valor, ordenado (Python 3.7+) | ✅ Sí |
| `deque` | Eficiente para inserción/eliminación en ambos extremos | ✅ Sí |
| `Counter` | Cuenta la frecuencia de elementos | ✅ Sí |
| `defaultdict` | Diccionario con valores por defecto | ✅ Sí |
| `OrderedDict` | Diccionario ordenado (Python <3.7) | ✅ Sí |

---

