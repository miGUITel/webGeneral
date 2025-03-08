### **Mutabilidad en Java**  

En **Java** también existen **tipos mutables e inmutables**, aunque el comportamiento y la forma de manejarlos son diferentes a **Python**.

---

## **🔹 Tipos Inmutables en Java**  
Los objetos **inmutables** en Java no pueden ser modificados después de su creación.  
Si intentamos cambiar su contenido, se **crea un nuevo objeto** en memoria.  

### **Ejemplos de tipos inmutables en Java**:
- **`String`** (cadenas de texto)
- **`Integer`, `Double`, `Float`, `Boolean`, `Character`** (Wrappers de tipos primitivos)
- **`BigInteger`, `BigDecimal`** (Clases de números grandes)
- **`LocalDate`, `LocalTime`, `LocalDateTime`** (Fechas en `java.time`)

---

### **Ejemplo en Java (Inmutabilidad de `String`)**
```java
public class Main {
    public static void main(String[] args) {
        String texto = "Hola";
        System.out.println(System.identityHashCode(texto)); // 📌 Dirección en memoria

        texto = texto + " mundo"; // Se crea un NUEVO objeto
        System.out.println(System.identityHashCode(texto)); // 📌 Nueva dirección en memoria
    }
}
```
**🔴 Problema**:  
Cada modificación de `String` genera **un nuevo objeto en memoria**, lo que **puede ser ineficiente** si se hacen muchas concatenaciones.  

✅ **Solución**: Usar `StringBuilder` o `StringBuffer` para modificar cadenas de forma **mutable**.
```java
StringBuilder sb = new StringBuilder("Hola");
sb.append(" mundo");
System.out.println(sb); // "Hola mundo"
```

---

## **🔹 Tipos Mutables en Java**  
Los objetos **mutables** pueden ser modificados sin necesidad de crear un nuevo objeto.

### **Ejemplos de tipos mutables en Java**:
- **`StringBuilder`, `StringBuffer`** (cadenas mutables)
- **`ArrayList`, `HashMap`, `HashSet`** (colecciones mutables)
- **`User-defined classes`** (Clases creadas por el usuario, a menos que se hagan inmutables)

---

### **Ejemplo en Java (Objeto Mutable con `ArrayList`)**
```java
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> lista = new ArrayList<>();
        System.out.println(System.identityHashCode(lista)); // 📌 Dirección en memoria

        lista.add("Elemento 1"); // Modifica el mismo objeto en memoria
        System.out.println(System.identityHashCode(lista)); // 📌 MISMA dirección en memoria
    }
}
```
✅ **El objeto `ArrayList` se modifica sin crear una nueva copia**.

---

## **🔹 ¿Cómo hacer una clase inmutable en Java?**  
Para crear una clase inmutable en Java, debemos asegurarnos de que:
1. **Todos sus atributos sean `private` y `final`**.
2. **No haya métodos `setter`**.
3. **Los objetos mutables dentro de la clase no se expongan directamente**.

### **Ejemplo de Clase Inmutable en Java**
```java
public final class Persona {
    private final String nombre;
    private final int edad;

    public Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public int getEdad() {
        return edad;
    }
}
```
✅ **No podemos modificar los atributos después de la creación del objeto**.

---

## **🔹 Diferencias entre Java y Python en Mutabilidad**
| Aspecto | Java | Python |
|---------|------|--------|
| **Modificadores de acceso** | ✅ `private`, `final` para restringir cambios | ❌ No hay `private` real, solo convenciones |
| **String es mutable?** | ❌ No (`String` es inmutable) | ❌ No (`str` es inmutable) |
| **Listas (`ArrayList` / `list`)** | ✅ Mutable (`ArrayList`) | ✅ Mutable (`list`) |
| **Clases inmutables** | ✅ Se pueden hacer con `final` y sin `setters` | ⚠️ Se pueden hacer, pero no hay `final` |

---

## **📌 Conclusión**
✔ **Java y Python manejan la mutabilidad de forma diferente**.  
✔ **En Java, `String` es inmutable**, lo que obliga a usar `StringBuilder` para cambios eficientes.  
✔ **Las colecciones (`ArrayList`, `HashMap`) son mutables en Java**, igual que `list` y `dict` en Python.  
✔ **Java permite controlar la mutabilidad con `final` y modificadores de acceso**, mientras que en Python se confía en convenciones.  
