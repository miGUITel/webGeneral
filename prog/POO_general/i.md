[SOLID](./solid.md)

### **I - Principio de Segregación de Interfaces (ISP - Interface Segregation Principle)**  

👉 **Definición:**  
*"Una clase no debe verse obligada a implementar interfaces que no usa."*  

Este principio nos dice que **es mejor tener varias interfaces pequeñas y específicas que una interfaz grande y genérica**. De esta manera, las clases solo implementan lo que realmente necesitan y no métodos innecesarios.

---

## **🔴 Mal diseño (Violación de ISP en Java)**  

Supongamos que tenemos una interfaz `Trabajador` que agrupa diferentes responsabilidades como programar y manejar clientes.

```java
interface Trabajador {
    void programar();
    void atenderCliente();
}
```

Ahora implementamos dos clases:

```java
class Programador implements Trabajador {
    @Override
    public void programar() {
        System.out.println("Escribiendo código...");
    }

    @Override
    public void atenderCliente() {
        throw new UnsupportedOperationException("Un programador no atiende clientes");
    }
}

class ServicioAlCliente implements Trabajador {
    @Override
    public void programar() {
        throw new UnsupportedOperationException("Un agente de servicio al cliente no programa");
    }

    @Override
    public void atenderCliente() {
        System.out.println("Atendiendo a un cliente...");
    }
}
```

### **❌ Problema:**
- **Programador** no debería implementar `atenderCliente()`.
- **ServicioAlCliente** no debería implementar `programar()`.
- **Cada clase implementa métodos innecesarios y los deja vacíos o lanzando excepciones**.
- **Esto viola ISP**, ya que **las clases están obligadas a implementar métodos que no necesitan**.

---

## **✅ Buen diseño (Aplicando ISP en Java)**  

Dividimos la interfaz en dos **interfaces más específicas**:  
1. `Desarrollador`, que solo tiene `programar()`.  
2. `AtencionAlCliente`, que solo tiene `atenderCliente()`.  

```java
interface Desarrollador {
    void programar();
}

interface AtencionAlCliente {
    void atenderCliente();
}

// Ahora cada clase solo implementa lo que necesita
class Programador implements Desarrollador {
    @Override
    public void programar() {
        System.out.println("Escribiendo código...");
    }
}

class ServicioAlCliente implements AtencionAlCliente {
    @Override
    public void atenderCliente() {
        System.out.println("Atendiendo a un cliente...");
    }
}
```

Ahora cada clase **solo implementa los métodos que necesita**, cumpliendo el principio ISP.

---

## **🔴 Mal diseño (Violación de ISP en Python)**  

Ahora veamos el mismo error en Python:

```python
class Trabajador:
    def programar(self):
        raise NotImplementedError()

    def atender_cliente(self):
        raise NotImplementedError()


class Programador(Trabajador):
    def programar(self):
        print("Escribiendo código...")

    def atender_cliente(self):
        raise NotImplementedError("Un programador no atiende clientes")


class ServicioAlCliente(Trabajador):
    def programar(self):
        raise NotImplementedError("Un agente de servicio al cliente no programa")

    def atender_cliente(self):
        print("Atendiendo a un cliente...")
```

### **❌ Problema:**
- `Programador` no debería implementar `atender_cliente()`.
- `ServicioAlCliente` no debería implementar `programar()`.
- **Cada clase implementa métodos innecesarios y los deja vacíos o con excepciones**.
- Esto **viola ISP** porque **las clases están obligadas a implementar métodos que no necesitan**.

---

## **✅ Buen diseño (Aplicando ISP en Python)**  

Dividimos la clase base en **múltiples clases abstractas más específicas**:

```python
from abc import ABC, abstractmethod

class Desarrollador(ABC):
    @abstractmethod
    def programar(self):
        pass

class AtencionAlCliente(ABC):
    @abstractmethod
    def atender_cliente(self):
        pass


class Programador(Desarrollador):
    def programar(self):
        print("Escribiendo código...")


class ServicioAlCliente(AtencionAlCliente):
    def atender_cliente(self):
        print("Atendiendo a un cliente...")
```

✅ Ahora cada clase solo implementa los métodos que realmente necesita.

---

## **✅ Ventajas de este enfoque**
- **Las clases no implementan métodos innecesarios**.  
- **Cada interfaz tiene una única responsabilidad** (similar a SRP).  
- **El código es más modular y fácil de mantener**.  

---

## **📌 Resumen**
✔ **Evita interfaces grandes y con métodos que no todas las clases necesitan.**  
✔ **Divide las interfaces en partes más pequeñas y específicas.**  
✔ **Cada clase solo debe implementar lo que realmente usa.**  

---

[SOLID](./solid.md)