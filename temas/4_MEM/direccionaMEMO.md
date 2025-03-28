## 4. Modos de direccionamiento de la memoria

### 4.1 Direccionamiento cableado
El direccionamiento cableado se basa en líneas físicas (cables) que activan filas y columnas de celdas de memoria. Cuantos más bits de dirección, más compleja es la red de interconexión.

#### 4.1.1 Direccionamiento 2D
- Organización en forma de matriz (filas y columnas).
- Cada celda se selecciona mediante la activación de una fila y una columna.
- Muy utilizado en memorias RAM convencionales.
- Eficiente y económico para memorias de tamaño medio.

#### 4.1.2 Direccionamiento 3D
- Añade una tercera dimensión (por ejemplo, capas).
- Se usa en memorias modernas de alta densidad como las 3D NAND.
- Permite almacenar más datos en menos espacio físico.
- Mejora la escalabilidad sin aumentar demasiado la superficie del chip.

### 4.2 Direccionamiento mediante contenido (CAM)
- CAM: *Content Addressable Memory* (memoria direccionada por contenido).
- En lugar de usar una dirección concreta, se accede buscando un dato.
- Útil en aplicaciones como:
  - Tablas de enrutamiento en redes.
  - Caches asociativas en procesadores.
- Más rápido para búsquedas, pero más costoso y complejo.

### 4.3 Esquemas mixtos y direccionamiento en memorias semiconductoras
- Muchas memorias actuales combinan técnicas.
- Las memorias semiconductoras como DRAM o SRAM utilizan direccionamiento cableado, pero optimizado electrónicamente.
- En tecnologías como DDR o LPDDR, el direccionamiento se controla mediante controladores avanzados que gestionan bancos, filas, columnas, etc.
- Este direccionamiento puede optimizar el acceso secuencial o aleatorio, según el tipo de aplicación.

