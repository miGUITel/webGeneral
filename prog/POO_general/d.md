[SOLID](./solid.md)

### **D - Principio de Inversión de Dependencias (DIP - Dependency Inversion Principle)**  

👉 **Definición:**  
*"Los módulos de alto nivel no deben depender de los módulos de bajo nivel. Ambos deben depender de abstracciones."*  

Este principio nos dice que **las clases no deberían depender directamente de implementaciones concretas, sino de abstracciones (interfaces o clases abstractas)**.  
Así evitamos acoplamiento fuerte y hacemos el código más flexible y fácil de modificar.

---

## **🔴 Mal diseño (Violación de DIP en Java)**  

Supongamos que tenemos una clase `Coche` que **depende directamente** de la implementación de `MotorGasolina`.

```java
class MotorGasolina {
    public void encender() {
        System.out.println("Motor de gasolina encendido");
    }
}

class Coche {
    private MotorGasolina motor;

    public Coche() {
        this.motor = new MotorGasolina(); // 🚨 Dependencia directa
    }

    public void arrancar() {
        motor.encender();
    }
}
```

### **❌ Problema:**
- `Coche` está **acoplado a `MotorGasolina`**.  
- Si queremos cambiar a `MotorElectrico`, tenemos que **modificar la clase `Coche`**, lo que **viola OCP y DIP**.
- No podemos reutilizar `Coche` con otro tipo de motor sin modificar su código.

---

## **✅ Buen diseño (Aplicando DIP en Java con interfaces)**  

Creamos una **interfaz `Motor`**, de la que `MotorGasolina` y `MotorElectrico` pueden derivar.  
Ahora `Coche` **depende de una abstracción** (`Motor`), no de una implementación concreta.

```java
// Se define una abstracción (interfaz) en lugar de una implementación concreta
interface Motor {
    void encender();
}

// Implementaciones concretas de Motor
class MotorGasolina implements Motor {
    public void encender() {
        System.out.println("Motor de gasolina encendido");
    }
}

class MotorElectrico implements Motor {
    public void encender() {
        System.out.println("Motor eléctrico encendido");
    }
}

// Coche ahora depende de la abstracción Motor
class Coche {
    private Motor motor;

    public Coche(Motor motor) {
        this.motor = motor;
    }

    public void arrancar() {
        motor.encender();
    }
}

// Uso
public class Main {
    public static void main(String[] args) {
        Coche cocheGasolina = new Coche(new MotorGasolina());
        cocheGasolina.arrancar();  // "Motor de gasolina encendido"

        Coche cocheElectrico = new Coche(new MotorElectrico());
        cocheElectrico.arrancar(); // "Motor eléctrico encendido"
    }
}
```

✅ **Ahora `Coche` no necesita modificaciones si queremos agregar nuevos tipos de motores.**  
✅ **Podemos cambiar `MotorGasolina` por `MotorElectrico` sin afectar la clase `Coche`**.  

---

## **🔴 Mal diseño (Violación de DIP en Python)**  

Ahora veamos el mismo problema en Python.

```python
class MotorGasolina:
    def encender(self):
        print("Motor de gasolina encendido")

class Coche:
    def __init__(self):
        self.motor = MotorGasolina()  # 🚨 Dependencia directa

    def arrancar(self):
        self.motor.encender()
```

### **❌ Problema:**
- `Coche` está **acoplado a `MotorGasolina`**, por lo que no podemos cambiarlo fácilmente.
- Si queremos usar otro motor, debemos **modificar la clase `Coche`**, lo que viola DIP.

---

## **✅ Buen diseño (Aplicando DIP en Python con abstracciones)**  

En su lugar, creamos una **clase abstracta `Motor`**, que define una interfaz común para todos los motores.

```python
from abc import ABC, abstractmethod

# Abstracción (Interfaz)
class Motor(ABC):
    @abstractmethod
    def encender(self):
        pass

# Implementaciones concretas de Motor
class MotorGasolina(Motor):
    def encender(self):
        print("Motor de gasolina encendido")

class MotorElectrico(Motor):
    def encender(self):
        print("Motor eléctrico encendido")

# Coche ahora depende de la abstracción Motor
class Coche:
    def __init__(self, motor: Motor):
        self.motor = motor

    def arrancar(self):
        self.motor.encender()

# Uso
coche_gasolina = Coche(MotorGasolina())
coche_gasolina.arrancar()  # "Motor de gasolina encendido"

coche_electrico = Coche(MotorElectrico())
coche_electrico.arrancar()  # "Motor eléctrico encendido"
```

✅ **Ahora `Coche` no depende de una implementación específica**.  
✅ **Podemos cambiar de `MotorGasolina` a `MotorElectrico` sin tocar la clase `Coche`**.  

---

## **✅ Ventajas de este enfoque**
- **Código desacoplado**: `Coche` no está ligado a una implementación concreta.
- **Fácil de extender**: Podemos agregar nuevos motores sin modificar `Coche`.
- **Más flexible**: Se puede cambiar el comportamiento en tiempo de ejecución.

---

## **📌 Resumen**
✔ **Las clases de alto nivel no deben depender de clases de bajo nivel, sino de abstracciones.**  
✔ **Las dependencias deben inyectarse, no crearse dentro de la clase.**  
✔ **Facilita la reutilización y el mantenimiento del código.**  

[SOLID](./solid.md)