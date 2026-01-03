# Estructura del PDF Generado

## Vista General

El generador crea documentos PDF profesionales con el siguiente diseño:

## Componentes del PDF

### 1. **Cabecera (Header)**
- **Logo**: Imagen centrada en la parte superior (200x80 px aprox.)
  - Color de fondo: #2c3e50 (azul oscuro)
  - Borde: #3498db (azul)
  - Texto "LOGO" en el centro
- **Título "FACTURA"**: 
  - Tamaño: 28pt
  - Fuente: Helvetica-Bold
  - Color: #2c3e50
  - Alineación: Centrado
- **Fecha de Emisión**:
  - Formato: DD/MM/YYYY
  - Se genera automáticamente al crear el PDF

### 2. **Tabla de Detalles de Gastos**

#### Encabezado de la Tabla
- Fondo: #2c3e50 (azul oscuro)
- Texto: Color blanco
- Fuente: Helvetica-Bold, 11pt
- Columnas:
  1. **Descripción**: Descripción del servicio/producto
  2. **Precio Unitario**: Precio por unidad en euros (€)
  3. **Unidades**: Cantidad
  4. **Total**: Total calculado en euros (€)
  5. **Validez**: Período de validez o garantía

#### Filas de Datos
- Colores alternados:
  - Blanco (#FFFFFF)
  - Gris claro (#ecf0f1)
- Fuente: Helvetica, 10pt
- Color del texto: #2c3e50
- Alineación:
  - Descripción: Izquierda
  - Precio Unitario: Derecha
  - Unidades: Centro
  - Total: Derecha
  - Validez: Centro
- Bordes: Gris (#7f8c8d), 0.5pt

### 3. **Sección de Total**
- **Fondo**: Rojo (#e74c3c) - Destacado
- **Borde**: Rojo oscuro (#c0392b), 2pt
- **Texto**: Blanco
- **Fuente**: Helvetica-Bold, 12pt
- **Contenido**:
  - Etiqueta "TOTAL:" alineada a la derecha
  - Monto total en euros con 2 decimales
  - Posición: Alineada con las columnas de la tabla

### 4. **Pie de Página (Footer)**
- **Fuente**: Helvetica, 9pt
- **Color**: Gris (#7f8c8d)
- **Alineación**: Centrado
- **Contenido**:
  - "Detalles Adicionales" (en negrita)
  - Nota sobre impuestos incluidos
  - Información sobre validez y garantía
  - Información de contacto
  - Mensaje de agradecimiento (en cursiva)

## Especificaciones Técnicas

### Formato del Documento
- **Tamaño de Página**: A4 (210 × 297 mm)
- **Márgenes**: 50 puntos en todos los lados
- **Orientación**: Vertical (Portrait)
- **Versión PDF**: 1.4

### Paleta de Colores
- **Azul Oscuro** (#2c3e50): Header, títulos
- **Azul Claro** (#3498db): Acentos, logo
- **Rojo** (#e74c3c): Total destacado
- **Rojo Oscuro** (#c0392b): Borde del total
- **Gris Oscuro** (#34495e): Texto secundario
- **Gris Claro** (#ecf0f1): Fondo alternado
- **Gris Medio** (#7f8c8d): Bordes, footer

### Tipografía
- **Principal**: Helvetica
- **Negrita**: Helvetica-Bold
- **Tamaños**:
  - Título: 28pt
  - Encabezados tabla: 11pt
  - Datos tabla: 10pt
  - Total: 12pt
  - Footer: 9pt

## Características de Diseño

### Espaciado
- **Entre logo y título**: 0.3 pulgadas
- **Después del título**: 0.1 pulgadas
- **Antes de la tabla**: 0.3 pulgadas
- **Después de la tabla**: 0.4 pulgadas
- **Antes del footer**: 0.5 pulgadas

### Padding de Tabla
- **Encabezado**: 12pt (arriba y abajo), 8pt (lados)
- **Datos**: 8pt (arriba y abajo), 8pt (lados)
- **Total**: 10pt (arriba y abajo), 8pt (lados)

### Anchos de Columna
1. Descripción: 2.5 pulgadas
2. Precio Unitario: 1.2 pulgadas
3. Unidades: 0.9 pulgadas
4. Total: 1.2 pulgadas
5. Validez: 1.0 pulgadas

**Total de ancho**: ~6.8 pulgadas (cabe en A4 con márgenes)

## Datos del CSV

### Formato Requerido
```csv
descripcion,precio_unitario,unidades,total,validez
Servicio 1,100.00,10,1000.00,30 días
Servicio 2,85.50,20,1710.00,45 días
```

### Campos
- **descripcion**: Texto libre (string)
- **precio_unitario**: Número decimal con 2 decimales
- **unidades**: Número entero o decimal
- **total**: Número decimal con 2 decimales (precio_unitario × unidades)
- **validez**: Texto libre (ej: "30 días", "60 días", etc.)

## Ejemplos de Uso

### Ejemplo 1: Factura de Servicios de Desarrollo
```bash
python generate_invoice.py data.csv factura_desarrollo.pdf
```

### Ejemplo 2: Factura con Logo Personalizado
```bash
python generate_invoice.py mis_datos.csv factura_2024.pdf mi_logo.png
```

### Ejemplo 3: Múltiples Facturas
```bash
python generate_invoice.py enero.csv factura_enero.pdf
python generate_invoice.py febrero.csv factura_febrero.pdf
python generate_invoice.py marzo.csv factura_marzo.pdf
```

## Limitaciones y Consideraciones

1. **Sin información de cliente**: El diseño actual no incluye campos para datos del cliente (nombre, dirección, etc.) debido a las limitaciones especificadas.

2. **Moneda fija**: Los precios se muestran en euros (€). Para cambiar la moneda, editar el código en `generate_invoice.py`.

3. **Tamaño de página**: Configurado para A4. Para cambiar a Carta (Letter), modificar `pagesize=A4` a `pagesize=letter`.

4. **Idioma**: Textos en español. Para internacionalización, considerar usar archivos de traducción.

5. **Logo**: Si no se proporciona un logo, se genera uno automáticamente como placeholder.

## Personalización Avanzada

Para personalizar colores, fuentes o diseño, editar las siguientes secciones en `generate_invoice.py`:

- **Colores**: Variables `colors.HexColor('#XXXXXX')`
- **Fuentes**: Variables con `fontName` y `fontSize`
- **Espaciado**: Variables con `Spacer(1, X*inch)`
- **Texto del footer**: Variable `footer_text`
