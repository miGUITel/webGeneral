[De números](#ejemplo-pedir-un-número-entero)

### 📌 **Entrada en Python: Cómo funciona y cómo se usa** 

En Python, la entrada de datos se realiza con la función `input()`, que permite al usuario ingresar información desde la consola. La función siempre devuelve un **string** (cadena de texto), por lo que si necesitas trabajar con números u otros tipos de datos, es necesario convertir la entrada.

---

## 🔹 **Uso básico de `input()`**
La sintaxis de `input()` es:
```python
variable = input("Mensaje para el usuario: ")
```
📌 **Ejemplo simple:**
```python
nombre = input("¿Cuál es tu nombre? ")
print("Hola,", nombre)
```
✍️ **Salida esperada (si el usuario escribe "Carlos")**:
```
¿Cuál es tu nombre? Carlos
Hola, Carlos
```

---

## 🔹 **Conversión de tipos en la entrada**
Dado que `input()` devuelve siempre una **cadena de texto**, si queremos trabajar con números, debemos hacer una conversión.

### 🟢 **1. Convertir entrada a un número entero (`int`)**
```python
edad = int(input("¿Cuántos años tienes? "))
print("Tendrás", edad + 1, "años el próximo año.")
```
✍️ **Entrada:** `25`  
✍️ **Salida:** `Tendrás 26 años el próximo año.`

🔴 **Cuidado**: Si el usuario ingresa algo que no es un número (`"hola"`), el programa generará un error.

---

### 🟢 **2. Convertir entrada a un número decimal (`float`)**
```python
altura = float(input("¿Cuál es tu altura en metros? "))
print("Tu altura es:", altura, "metros.")
```
✍️ **Entrada:** `1.75`  
✍️ **Salida:** `Tu altura es: 1.75 metros.`

---

## 🔹 **Manejo de errores en la entrada (`try-except`)**
Para evitar que el programa falle si el usuario ingresa datos incorrectos, usamos `try-except`:

```python
try:
    numero = int(input("Introduce un número entero: "))
    print("El número ingresado es:", numero)
except ValueError:
    print("Error: No has introducido un número válido.")
```
🔹 **Si el usuario escribe "hola" en lugar de un número, el programa mostrará:**
```
Error: No has introducido un número válido.
```
💡 **Siempre es recomendable manejar excepciones cuando se espera un número.**

---

## 🔹 **Entrada múltiple en una sola línea**
Si queremos que el usuario ingrese varios valores en una sola línea, podemos usar `split()`:

```python
a, b = input("Introduce dos números separados por espacio: ").split()
a = int(a)
b = int(b)
print("La suma es:", a + b)
```
📌 **Entrada:** `4 5`  
📌 **Salida:** `La suma es: 9`

📌 También podemos convertir todos los valores de una vez:
```python
numeros = list(map(int, input("Introduce tres números separados por espacio: ").split()))
print("Has ingresado:", numeros)
```
📌 **Entrada:** `3 7 9`  
📌 **Salida:** `Has ingresado: [3, 7, 9]`

---

## 🔹 **Lectura de entrada sin mostrar mensaje (`sys.stdin.readline`)**
En programas donde la eficiencia es clave (como concursos de programación), `sys.stdin.readline()` es más rápido que `input()`:

```python
import sys
dato = sys.stdin.readline().strip()  # .strip() elimina espacios y saltos de línea
print("Ingresaste:", dato)
```
Este método es útil cuando se esperan **grandes volúmenes de datos**.

---

## 🔹 **Entrada en bucles (`while`)**
Si queremos asegurarnos de que el usuario ingrese un dato válido, podemos usar un bucle:

```python
while True:
    try:
        numero = int(input("Introduce un número positivo: "))
        if numero > 0:
            break
        else:
            print("El número debe ser positivo.")
    except ValueError:
        print("Por favor, introduce un número válido.")
```

---

## 🔹 **Resumen**
✔ `input()` siempre devuelve una cadena de texto.  
✔ Convierte la entrada con `int()` o `float()` si necesitas números.  
✔ Usa `try-except` para manejar errores y evitar que el programa se bloquee.  
✔ Puedes pedir múltiples valores en una sola línea con `split()`.  
✔ Para grandes volúmenes de datos, `sys.stdin.readline()` es más eficiente.  
✔ Usa bucles para validar la entrada y asegurarte de que el usuario ingresa datos correctos.

💡 ¡Ahora ya sabes cómo manejar la entrada en Python de forma segura y eficiente! 🚀

En Python, la entrada de datos se obtiene con la función `input()`, que siempre devuelve un **string** (cadena de texto). Si necesitas preguntar al usuario un número, debes convertir esa entrada a un tipo numérico como `int` o `float`.

### Ejemplo: Pedir un número entero
```python
numero = int(input("Introduce un número: "))
print("Has introducido el número:", numero)
```
🔹 **Explicación**:
- `input("Introduce un número: ")` muestra el mensaje en la consola y espera la entrada del usuario.
- `int(...)` convierte la entrada de texto en un número entero.
- `print(...)` muestra el resultado.

### Manejo de números decimales (`float`)
Si necesitas un número con decimales:
```python
numero_decimal = float(input("Introduce un número decimal: "))
print("Has introducido:", numero_decimal)
```

### Manejo de errores con `try-except`
Para evitar que el programa falle si el usuario introduce algo que no es un número, usa `try-except`:
```python
try:
    numero = int(input("Introduce un número entero: "))
    print("El número ingresado es:", numero)
except ValueError:
    print("Error: No has introducido un número válido.")
```
🔹 **Explicación**:
- `try` intenta ejecutar la conversión a entero.
- Si el usuario introduce algo que no puede convertirse (`"abc"`, `"3.5"`, etc.), `except ValueError` captura el error y muestra un mensaje.

✅ Ahora puedes pedir números al usuario de forma segura y sin errores inesperados. 🚀