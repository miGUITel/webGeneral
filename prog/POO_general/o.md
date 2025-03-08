[SOLID](./solid.md)

### **O - Principio de Abierto/Cerrado (OCP - Open/Closed Principle)**  

👉 **Definición:**  
*"Las clases deben estar **abiertas para extensión, pero cerradas para modificación**."*  

Este principio establece que **deberíamos poder añadir nuevas funcionalidades sin modificar el código existente**. En lugar de cambiar una clase cada vez que necesitemos una nueva funcionalidad, deberíamos **extenderla** mediante herencia o polimorfismo.

---

## **🔴 Mal diseño (Violación de OCP)**  

Supongamos que tenemos una clase `CalculadoraDescuentos`, que calcula descuentos para distintos tipos de clientes (`estudiante`, `vip`, `normal`).  

```python
class CalculadoraDescuentos:
    def calcular(self, tipo_cliente, precio):
        if tipo_cliente == "estudiante":
            return precio * 0.9  # 10% de descuento
        elif tipo_cliente == "vip":
            return precio * 0.8  # 20% de descuento
        elif tipo_cliente == "normal":
            return precio  # Sin descuento
        else:
            raise ValueError("Tipo de cliente no válido")
```

**❌ Problema:**  
- Cada vez que agregamos un nuevo tipo de cliente (ej. "mayor de 65 años"), debemos modificar la clase.  
- Esto viola **OCP**, porque la clase no está **cerrada para modificaciones**.  
- El código se vuelve **difícil de mantener y propenso a errores**.

---

## **✅ Buen diseño (Aplicando OCP con polimorfismo)**  

En lugar de modificar la clase cada vez que agregamos un nuevo tipo de cliente, creamos una **clase base** y extendemos su funcionalidad con **nuevas clases**.

```python
from abc import ABC, abstractmethod

# Definimos una interfaz para los descuentos
class Descuento(ABC):
    @abstractmethod
    def aplicar(self, precio):
        pass

# Implementamos diferentes tipos de descuento
class DescuentoEstudiante(Descuento):
    def aplicar(self, precio):
        return precio * 0.9  # 10% de descuento

class DescuentoVIP(Descuento):
    def aplicar(self, precio):
        return precio * 0.8  # 20% de descuento

class DescuentoNormal(Descuento):
    def aplicar(self, precio):
        return precio  # Sin descuento

# Ahora la Calculadora de descuentos ya no necesita modificaciones
class CalculadoraDescuentos:
    def __init__(self, estrategia_descuento: Descuento):
        self.estrategia_descuento = estrategia_descuento

    def calcular(self, precio):
        return self.estrategia_descuento.aplicar(precio)

# Uso
precio_original = 100
cliente_vip = CalculadoraDescuentos(DescuentoVIP()) //un costructor(que recibe otro())
print(cliente_vip.calcular(precio_original))  # 80€

cliente_estudiante = CalculadoraDescuentos(DescuentoEstudiante())
print(cliente_estudiante.calcular(precio_original))  # 90€
```

---

## **✅ Ventajas de este enfoque**
- **La clase `CalculadoraDescuentos` nunca se modifica**, solo se **extiende** con nuevas clases.
- Podemos agregar más tipos de descuentos sin tocar el código existente.
- Favorece el **polimorfismo** y el **principio de responsabilidad única (SRP)**.

---

## **📌 Resumen**
✔ **Las clases deben poder extenderse sin necesidad de modificarlas**.  
✔ **Usar polimorfismo** para evitar modificar clases existentes.  
✔ Facilita el mantenimiento y evita introducir errores en código ya probado.  

---

## java:

### **O - Principio de Abierto/Cerrado (OCP - Open/Closed Principle) en Java**  

👉 **Definición:**  
*"Las clases deben estar **abiertas para extensión, pero cerradas para modificación**."*  

Esto significa que **deberíamos poder añadir nuevas funcionalidades sin modificar el código existente**. En lugar de cambiar una clase cada vez que necesitemos una nueva funcionalidad, deberíamos **extenderla** mediante herencia o polimorfismo.

---

## **🔴 Mal diseño (Violación de OCP en Java)**  

Supongamos que tenemos una clase `CalculadoraDescuentos`, que calcula descuentos para distintos tipos de clientes (`estudiante`, `vip`, `normal`).  

```java
public class CalculadoraDescuentos {
    public double calcular(String tipoCliente, double precio) {
        if (tipoCliente.equals("estudiante")) {
            return precio * 0.9; // 10% de descuento
        } else if (tipoCliente.equals("vip")) {
            return precio * 0.8; // 20% de descuento
        } else if (tipoCliente.equals("normal")) {
            return precio; // Sin descuento
        } else {
            throw new IllegalArgumentException("Tipo de cliente no válido");
        }
    }
}
```

**❌ Problema:**  
- Cada vez que agregamos un nuevo tipo de cliente (ej. "mayor de 65 años"), debemos modificar la clase.  
- Esto viola **OCP**, porque la clase no está **cerrada para modificaciones**.  
- El código se vuelve **difícil de mantener y propenso a errores**.

---

## **✅ Buen diseño (Aplicando OCP con polimorfismo en Java)**  

En lugar de modificar la clase cada vez que agregamos un nuevo tipo de cliente, creamos una **interfaz** y **extendemos** su funcionalidad con **clases concretas**.

```java
// Interfaz para aplicar descuentos
interface Descuento {
    double aplicar(double precio);
}

// Implementaciones de la interfaz Descuento
class DescuentoEstudiante implements Descuento {
    public double aplicar(double precio) {
        return precio * 0.9; // 10% de descuento
    }
}

class DescuentoVIP implements Descuento {
    public double aplicar(double precio) {
        return precio * 0.8; // 20% de descuento
    }
}

class DescuentoNormal implements Descuento {
    public double aplicar(double precio) {
        return precio; // Sin descuento
    }
}

// Clase CalculadoraDescuentos que usa el polimorfismo
class CalculadoraDescuentos {
    private Descuento estrategiaDescuento;

    public CalculadoraDescuentos(Descuento estrategiaDescuento) {
        this.estrategiaDescuento = estrategiaDescuento;
    }

    public double calcular(double precio) {
        return estrategiaDescuento.aplicar(precio);
    }
}

// Uso de la CalculadoraDescuentos
public class Main {
    public static void main(String[] args) {
        double precioOriginal = 100.0;

        CalculadoraDescuentos clienteVIP = new CalculadoraDescuentos(new DescuentoVIP());
        System.out.println(clienteVIP.calcular(precioOriginal)); // 80.0

        CalculadoraDescuentos clienteEstudiante = new CalculadoraDescuentos(new DescuentoEstudiante());
        System.out.println(clienteEstudiante.calcular(precioOriginal)); // 90.0
    }
}
```

---

## **✅ Ventajas de este enfoque**
- **La clase `CalculadoraDescuentos` nunca se modifica**, solo se **extiende** con nuevas clases.
- Podemos agregar más tipos de descuentos sin tocar el código existente.
- Favorece el **polimorfismo** y el **principio de responsabilidad única (SRP)**.
- Facilita la reutilización del código.

---

## **📌 Resumen**
✔ **Las clases deben poder extenderse sin necesidad de modificarlas**.  
✔ **Usar polimorfismo** para evitar modificar clases existentes.  
✔ Facilita el mantenimiento y evita introducir errores en código ya probado.  

[SOLID](./solid.md)