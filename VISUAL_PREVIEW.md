# Visual Preview of Generated Invoice PDF

## Sample Invoice Layout

```
╔═══════════════════════════════════════════════════════════════════════╗
║                                                                       ║
║                    ┌─────────────────────────────┐                   ║
║                    │       [LOGO IMAGE]          │                   ║
║                    │    (200x80 pixels)          │                   ║
║                    └─────────────────────────────┘                   ║
║                                                                       ║
║                           FACTURA                                    ║
║                        (28pt, Bold)                                  ║
║                                                                       ║
║                    Fecha: 03/01/2026                                 ║
║                                                                       ║
║  ┌───────────────────────────────────────────────────────────────┐  ║
║  │ Descripción      │Precio Unit.│ Unidades │  Total  │ Validez │  ║
║  ├───────────────────────────────────────────────────────────────┤  ║
║  │ Consultoría de   │  €85.00    │    40    │€3400.00 │ 30 días │  ║
║  │ Desarrollo       │            │          │         │         │  ║
║  ├───────────────────────────────────────────────────────────────┤  ║
║  │ Diseño de        │  €95.00    │    25    │€2375.00 │ 45 días │  ║
║  │ Interface UI/UX  │            │          │         │         │  ║
║  ├───────────────────────────────────────────────────────────────┤  ║
║  │ Mantenimiento y  │  €60.00    │    15    │ €900.00 │ 60 días │  ║
║  │ Soporte          │            │          │         │         │  ║
║  ├───────────────────────────────────────────────────────────────┤  ║
║  │ Integración de   │  €75.00    │    20    │€1500.00 │ 30 días │  ║
║  │ API              │            │          │         │         │  ║
║  ├───────────────────────────────────────────────────────────────┤  ║
║  │ Testing y QA     │  €65.00    │    18    │€1170.00 │ 30 días │  ║
║  └───────────────────────────────────────────────────────────────┘  ║
║                                                                       ║
║                    ┌─────────────────────────────┐                   ║
║                    │       TOTAL: €9345.00       │                   ║
║                    │    (Highlighted in Red)     │                   ║
║                    └─────────────────────────────┘                   ║
║                                                                       ║
║                     Detalles Adicionales                             ║
║                                                                       ║
║          Todos los precios incluyen impuestos aplicables.            ║
║     La validez indicada corresponde al período de garantía o         ║
║                       soporte del servicio.                          ║
║         Para cualquier consulta, no dude en contactarnos.            ║
║                                                                       ║
║                    Gracias por su confianza.                         ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝
```

## Color Scheme

- **Header Background**: Dark Blue (#2c3e50)
- **Title**: Dark Blue (#2c3e50)
- **Table Header**: Dark Blue background (#2c3e50) with White text
- **Table Rows**: Alternating White and Light Gray (#ecf0f1)
- **Total Section**: Red background (#e74c3c) with Red border (#c0392b)
- **Footer**: Gray text (#7f8c8d)

## Key Features Visible in PDF

1. **Professional Layout**: Clean, organized structure with proper spacing
2. **Brand Identity**: Logo placeholder at the top (customizable)
3. **Clear Typography**: Helvetica family fonts with appropriate sizes
4. **Data Organization**: Well-structured table with 5 columns
5. **Visual Hierarchy**: Bold headers, clear separations, highlighted totals
6. **Professional Colors**: Blue and red color scheme for business documents
7. **Comprehensive Details**: All expense information clearly displayed
8. **Footer Information**: Additional context and professional closing

## Sample Data Displayed

From `data.csv`:
- 5 line items of services
- Total amount: €9,345.00
- Validity periods: 30-60 days
- Various service types: Development, Design, Maintenance, API, Testing

## Generated PDF Specifications

- **File Size**: ~4.5 KB
- **Pages**: 1
- **Format**: PDF 1.4
- **Page Size**: A4 (210 × 297 mm)
- **Resolution**: Standard PDF (vector graphics)

## How to View

After running the generator:
```bash
python generate_invoice.py
```

Open the generated `factura.pdf` with any PDF viewer:
- Adobe Acrobat Reader
- macOS Preview
- Linux: Evince, Okular
- Windows: Edge, Chrome, or PDF Reader
- Web browsers: Chrome, Firefox, Safari

The PDF will display all elements with proper formatting, colors, and professional appearance suitable for business use.
