[SOLID](./solid.md)

### **S - Principio de Responsabilidad Única (SRP - Single Responsibility Principle)**

👉 **Definición:**  
*"Una clase debe tener una única razón para cambiar."*  

Esto significa que **cada clase debe tener una única responsabilidad bien definida**. Si una clase tiene múltiples motivos para cambiar, es una señal de que está haciendo demasiado y debería dividirse en varias clases más pequeñas.

---

### **🔴 Mal diseño (Violación de SRP)**
Supongamos que tenemos una clase `GestorEmpleado` que **almacena datos de empleados y también genera reportes**.

```python
class GestorEmpleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_impuestos(self):
        return self.salario * 0.20  # 20% de impuestos

    def generar_reporte(self):
        return f"Reporte de {self.nombre}, salario: {self.salario}€"
```

**❌ Problema:**  
- La clase tiene **dos responsabilidades**:  
  1. **Gestionar los datos del empleado y calcular impuestos**.  
  2. **Generar reportes**.  
- Si cambian los cálculos de impuestos, debemos modificar la misma clase.  
- Si cambia la forma de generar reportes, también modificamos la misma clase.  
- Esto hace que el código sea **difícil de mantener**.

---

### **✅ Buen diseño (Aplicando SRP)**

Para seguir **SRP**, debemos dividir la clase en **dos clases separadas**:

```python
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_impuestos(self):
        return self.salario * 0.20  # 20% de impuestos


class ReporteEmpleado:
    @staticmethod
    def generar(empleado):
        return f"Reporte de {empleado.nombre}, salario: {empleado.salario}€"

# Uso
empleado = Empleado("Juan", 3000)
print(empleado.calcular_impuestos())  # 600€
print(ReporteEmpleado.generar(empleado))  # "Reporte de Juan, salario: 3000€"
```

**✅ Ventajas:**
- **Separación de responsabilidades**:  
  - `Empleado` solo gestiona datos y cálculos de impuestos.  
  - `ReporteEmpleado` solo se encarga de generar reportes.  
- **Facilita mantenimiento**:  
  - Si cambia la forma de calcular impuestos, solo modificamos `Empleado`.  
  - Si cambia el formato de los reportes, solo cambiamos `ReporteEmpleado`.  
- **Código más modular y reutilizable**.

---

### **📌 Resumen**
✔ **Cada clase debe hacer solo una cosa** y tener **una sola razón para cambiar**.  
✔ Separar responsabilidades mejora la **mantenibilidad** y **reutilización** del código.  
✔ Facilita la aplicación de otros principios **SOLID** y el **principio de separación de preocupaciones (SoC - Separation of Concerns)**.

---

[SOLID](./solid.md)