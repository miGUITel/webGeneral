[SOLID](./solid.md)

### **L - Principio de Sustitución de Liskov (LSP - Liskov Substitution Principle)**  

👉 **Definición:**  
*"Los objetos de una subclase deben poder reemplazar a los de su superclase sin alterar el comportamiento del programa."*  

Esto significa que **una subclase debe ser completamente intercambiable con su clase base**, sin necesidad de modificar el código que la usa.

---

## **🔴 Mal diseño (Violación de LSP en Java)**  

Supongamos que tenemos una **clase base `Rectangulo`** y una **subclase `Cuadrado`**.  
El problema surge porque **un cuadrado no se comporta exactamente como un rectángulo**, ya que sus lados siempre deben ser iguales.

```java
class Rectangulo {
    protected int ancho;
    protected int alto;

    public void setAncho(int ancho) {
        this.ancho = ancho;
    }

    public void setAlto(int alto) {
        this.alto = alto;
    }

    public int getArea() {
        return ancho * alto;
    }
}

class Cuadrado extends Rectangulo {
    @Override
    public void setAncho(int ancho) {
        this.ancho = ancho;
        this.alto = ancho; // 🚨 Rompe la lógica original del rectángulo
    }

    @Override
    public void setAlto(int alto) {
        this.alto = alto;
        this.ancho = alto; // 🚨 Rompe la lógica original del rectángulo
    }
}
```

### **❌ Problema:**  
- En la clase `Cuadrado`, cuando **cambiamos el ancho**, **automáticamente se cambia la altura**.
- Esto **rompe el comportamiento esperado** de `Rectangulo`, porque ahora el método `getArea()` podría devolver valores inesperados en ciertos contextos.
- Si un código espera trabajar con `Rectangulo`, pero recibe `Cuadrado`, podría fallar.

### **🔴 Ejemplo de fallo**
```java
public class Main {
    public static void main(String[] args) {
        Rectangulo r = new Cuadrado(); // 🚨 Se supone que es un rectángulo
        r.setAncho(5);
        r.setAlto(10); 
        System.out.println("Área: " + r.getArea()); // 🤔 Debería ser 50, pero será 100
    }
}
```

---

## **✅ Buen diseño (Aplicando LSP en Java)**
En lugar de heredar de `Rectangulo`, creamos una **clase base `Forma`** con un método abstracto `getArea()`. Esto garantiza que **cada forma implemente su propio cálculo de área sin afectar a otras clases**.

```java
abstract class Forma {
    public abstract int getArea();
}

class Rectangulo extends Forma {
    private int ancho;
    private int alto;

    public Rectangulo(int ancho, int alto) {
        this.ancho = ancho;
        this.alto = alto;
    }

    public int getArea() {
        return ancho * alto;
    }
}

class Cuadrado extends Forma {
    private int lado;

    public Cuadrado(int lado) {
        this.lado = lado;
    }

    public int getArea() {
        return lado * lado;
    }
}

// Uso
public class Main {
    public static void main(String[] args) {
        Forma rectangulo = new Rectangulo(5, 10);
        Forma cuadrado = new Cuadrado(5);

        System.out.println("Área del rectángulo: " + rectangulo.getArea()); // 50
        System.out.println("Área del cuadrado: " + cuadrado.getArea()); // 25
    }
}
```

**✅ Ahora ambas clases son intercambiables sin romper el comportamiento esperado.**  

---

## **🔴 Mal diseño (Violación de LSP en Python)**  

Ahora veamos el mismo error en Python.

```python
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def set_ancho(self, ancho):
        self.ancho = ancho

    def set_alto(self, alto):
        self.alto = alto

    def get_area(self):
        return self.ancho * self.alto


class Cuadrado(Rectangulo):
    def set_ancho(self, ancho):
        self.ancho = ancho
        self.alto = ancho  # 🚨 Problema: Al modificar el ancho, también cambia la altura

    def set_alto(self, alto):
        self.alto = alto
        self.ancho = alto  # 🚨 Problema: Al modificar la altura, también cambia el ancho


# Uso incorrecto
r = Cuadrado(5, 10)  # 🚨 Se supone que es un Rectángulo
r.set_ancho(5)
r.set_alto(10)
print("Área:", r.get_area())  # 🤔 Debería ser 50, pero será 100
```

### **❌ Problema:**
- `Cuadrado` **rompe la lógica del rectángulo** porque **modificar el ancho también cambia la altura**.
- Si un programa espera un `Rectangulo` pero recibe un `Cuadrado`, los resultados serán inesperados.

---

## **✅ Buen diseño (Aplicando LSP en Python)**  
En lugar de hacer que `Cuadrado` herede de `Rectangulo`, creamos una **clase base `Forma`** con un método `get_area()` para que cada forma implemente su propio cálculo.

```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def get_area(self):
        pass


class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def get_area(self):
        return self.ancho * self.alto


class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def get_area(self):
        return self.lado * self.lado


# Uso correcto
rectangulo = Rectangulo(5, 10)
cuadrado = Cuadrado(5)

print("Área del rectángulo:", rectangulo.get_area())  # 50
print("Área del cuadrado:", cuadrado.get_area())  # 25
```

---

## **✅ Ventajas de este enfoque**
- **Cada clase implementa su propia lógica sin romper la clase base.**
- **El código es más claro y predecible.**
- **Cumple con el principio LSP, permitiendo que cualquier `Forma` sea intercambiable.**

---

## **📌 Resumen**
✔ **Una subclase debe poder sustituir a su superclase sin cambiar el comportamiento esperado.**  
✔ **No todas las relaciones "es un" son correctas en la herencia.**  
✔ **Es mejor diseñar una jerarquía basada en abstracción que en herencia forzada.**  

---

[SOLID](./solid.md)