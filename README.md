# Generador de Facturas Profesionales (PDF Invoice Generator)

Este proyecto genera documentos PDF de facturas profesionales basados en datos de archivos CSV.

## Características

- ✨ Diseño profesional y limpio
- 📊 Tabla de detalles de gastos con información estructurada
- 🎨 Cabecera con logo personalizable y título "Factura"
- 💰 Pie de página con el total de costes resaltado
- 📅 Fecha automática
- 🎯 Información adicional y detalles relevantes

## Estructura de Datos CSV

El archivo CSV debe contener las siguientes columnas:

- `descripcion`: Descripción del servicio o producto
- `precio_unitario`: Precio por unidad
- `unidades`: Cantidad de unidades
- `total`: Total calculado (precio_unitario × unidades)
- `validez`: Período de validez o garantía

### Ejemplo de CSV (data.csv)

```csv
descripcion,precio_unitario,unidades,total,validez
Consultoría de Desarrollo,85.00,40,3400.00,30 días
Diseño de Interface UI/UX,95.00,25,2375.00,45 días
Mantenimiento y Soporte,60.00,15,900.00,60 días
```

## Instalación

### Requisitos Previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Instalar Dependencias

```bash
pip install -r requirements.txt
```

## Uso

### Uso Básico

Genera una factura usando el archivo `data.csv` por defecto:

```bash
python generate_invoice.py
```

Esto creará un archivo `factura.pdf` en el directorio actual.

### Uso Avanzado

Puedes especificar archivos personalizados:

```bash
python generate_invoice.py <archivo_csv> <salida_pdf> <archivo_logo>
```

**Ejemplos:**

```bash
# Usar un CSV personalizado
python generate_invoice.py mis_datos.csv mi_factura.pdf

# Especificar CSV, PDF de salida y logo personalizado
python generate_invoice.py datos.csv invoice_2024.pdf mi_logo.png
```

### Parámetros

1. **archivo_csv** (opcional): Ruta al archivo CSV con los datos de gastos. Por defecto: `data.csv`
2. **salida_pdf** (opcional): Nombre del archivo PDF de salida. Por defecto: `factura.pdf`
3. **archivo_logo** (opcional): Ruta a la imagen del logo. Por defecto: `logo.png` (se crea automáticamente si no existe)

## Logo Personalizado

Puedes usar tu propio logo:

1. Prepara una imagen en formato PNG o JPG
2. Recomendado: Tamaño aproximado 200x80 píxeles o similar proporción
3. Especifica la ruta al generar la factura:

```bash
python generate_invoice.py data.csv factura.pdf mi_logo_empresa.png
```

Si no proporcionas un logo, el script generará automáticamente un logo placeholder simple.

## Formato del PDF Generado

El PDF incluye:

### 1. Cabecera
- Logo de la empresa (centrado)
- Título "FACTURA" en formato destacado
- Fecha de emisión

### 2. Tabla de Detalles
- Descripción del servicio/producto
- Precio unitario (€)
- Cantidad de unidades
- Total por línea (€)
- Período de validez

### 3. Total Resaltado
- Suma total de todos los gastos
- Formato destacado con fondo rojo

### 4. Pie de Página
- Información adicional sobre impuestos
- Detalles sobre validez y garantía
- Mensaje de agradecimiento

## Personalización

El script está diseñado para ser fácilmente personalizable. Puedes modificar:

- Colores del tema (variables HexColor en el código)
- Tamaños de fuente
- Espaciado y márgenes
- Textos del pie de página
- Formato de la tabla

## Estructura del Proyecto

```
docs-generator/
│
├── generate_invoice.py    # Script principal
├── requirements.txt       # Dependencias de Python
├── data.csv              # Datos de ejemplo
├── logo.png              # Logo (generado automáticamente)
├── factura.pdf           # PDF generado (después de ejecutar)
└── README.md             # Este archivo
```

## Dependencias

- **reportlab**: Biblioteca para generación de PDFs
- **Pillow**: Biblioteca para manejo de imágenes

## Solución de Problemas

### Error: "CSV file not found"
- Verifica que el archivo CSV existe en la ruta especificada
- Asegúrate de usar la ruta correcta (absoluta o relativa)

### Error de importación
- Ejecuta: `pip install -r requirements.txt`
- Verifica que tienes Python 3.7 o superior: `python --version`

### El logo no aparece
- Verifica que el archivo de imagen existe
- Formatos soportados: PNG, JPG, GIF
- Si no hay logo, se generará uno automáticamente

## Licencia

Este proyecto es de código abierto y está disponible para uso personal y comercial.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request para sugerencias o mejoras.

## Autor

Desarrollado para generar facturas profesionales de manera rápida y eficiente.
