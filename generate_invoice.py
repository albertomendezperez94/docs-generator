#!/usr/bin/env python3
"""
Professional Invoice PDF Generator
Generates a professional invoice PDF from CSV data with logo, table, and totals.
"""

import csv
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_LEFT
import os


def create_logo_placeholder(filename='logo.png'):
    """Create a simple placeholder logo if it doesn't exist."""
    if not os.path.exists(filename):
        from PIL import Image, ImageDraw, ImageFont
        
        # Create a simple logo placeholder
        img = Image.new('RGB', (200, 80), color='#2c3e50')
        draw = ImageDraw.Draw(img)
        
        # Draw a simple design
        draw.rectangle([10, 10, 190, 70], outline='#3498db', width=3)
        
        # Try to add text
        try:
            font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 24)
            draw.text((100, 40), 'LOGO', anchor='mm', fill='#3498db', font=font)
        except:
            # If font is not available, just use the rectangle
            pass
        
        img.save(filename)
        print(f"Created placeholder logo: {filename}")


def read_csv_data(csv_file):
    """Read expense data from CSV file."""
    data = []
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def create_invoice_pdf(csv_file='data.csv', output_file='factura.pdf', logo_file='logo.png'):
    """
    Generate a professional invoice PDF from CSV data.
    
    Args:
        csv_file: Path to CSV file with expense data
        output_file: Output PDF filename
        logo_file: Path to logo image file
    """
    
    # Create logo if it doesn't exist
    create_logo_placeholder(logo_file)
    
    # Read CSV data
    expense_data = read_csv_data(csv_file)
    
    # Create PDF document
    doc = SimpleDocTemplate(
        output_file,
        pagesize=A4,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50
    )
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=12,
        textColor=colors.HexColor('#34495e'),
        spaceAfter=12,
        fontName='Helvetica-Bold'
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#2c3e50'),
    )
    
    # Add logo and title in header
    if os.path.exists(logo_file):
        logo = Image(logo_file, width=2*inch, height=0.8*inch)
        logo.hAlign = 'CENTER'
        elements.append(logo)
        elements.append(Spacer(1, 0.3*inch))
    
    # Add title
    title = Paragraph("<b>FACTURA</b>", title_style)
    elements.append(title)
    elements.append(Spacer(1, 0.1*inch))
    
    # Add invoice date
    current_date = datetime.now().strftime("%d/%m/%Y")
    date_text = Paragraph(f"<b>Fecha:</b> {current_date}", normal_style)
    elements.append(date_text)
    elements.append(Spacer(1, 0.3*inch))
    
    # Create table with expense details
    # Table headers
    table_data = [
        ['Descripción', 'Precio Unitario', 'Unidades', 'Total', 'Validez']
    ]
    
    # Add data rows
    total_cost = 0.0
    for item in expense_data:
        row = [
            item.get('descripcion', ''),
            f"€{float(item.get('precio_unitario', 0)):.2f}",
            item.get('unidades', ''),
            f"€{float(item.get('total', 0)):.2f}",
            item.get('validez', '')
        ]
        table_data.append(row)
        total_cost += float(item.get('total', 0))
    
    # Create table
    table = Table(table_data, colWidths=[2.5*inch, 1.2*inch, 0.9*inch, 1.2*inch, 1*inch])
    
    # Style the table
    table_style = TableStyle([
        # Header styling
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c3e50')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        
        # Data rows styling
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#2c3e50')),
        ('ALIGN', (1, 1), (1, -1), 'RIGHT'),  # Price unit right aligned
        ('ALIGN', (2, 1), (2, -1), 'CENTER'),  # Units centered
        ('ALIGN', (3, 1), (3, -1), 'RIGHT'),  # Total right aligned
        ('ALIGN', (4, 1), (4, -1), 'CENTER'),  # Validity centered
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        
        # Grid
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#7f8c8d')),
        
        # Alternating row colors
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#ecf0f1')]),
    ])
    
    table.setStyle(table_style)
    elements.append(table)
    elements.append(Spacer(1, 0.4*inch))
    
    # Add total section (highlighted)
    total_data = [
        ['', '', '', 'TOTAL:', f"€{total_cost:.2f}"]
    ]
    
    total_table = Table(total_data, colWidths=[2.5*inch, 1.2*inch, 0.9*inch, 1.2*inch, 1*inch])
    total_table_style = TableStyle([
        ('BACKGROUND', (3, 0), (-1, 0), colors.HexColor('#e74c3c')),
        ('TEXTCOLOR', (3, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (3, 0), (3, 0), 'RIGHT'),
        ('ALIGN', (4, 0), (4, 0), 'RIGHT'),
        ('FONTNAME', (3, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (3, 0), (-1, 0), 12),
        ('TOPPADDING', (3, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (3, 0), (-1, 0), 10),
        ('LEFTPADDING', (0, 0), (-1, 0), 8),
        ('RIGHTPADDING', (0, 0), (-1, 0), 8),
        ('BOX', (3, 0), (-1, 0), 2, colors.HexColor('#c0392b')),
    ])
    total_table.setStyle(total_table_style)
    elements.append(total_table)
    
    # Add footer information
    elements.append(Spacer(1, 0.5*inch))
    
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#7f8c8d'),
        alignment=TA_CENTER,
    )
    
    footer_text = """
    <para alignment="center">
    <b>Detalles Adicionales</b><br/>
    Todos los precios incluyen impuestos aplicables.<br/>
    La validez indicada corresponde al período de garantía o soporte del servicio.<br/>
    Para cualquier consulta, no dude en contactarnos.<br/>
    <br/>
    <i>Gracias por su confianza.</i>
    </para>
    """
    
    footer = Paragraph(footer_text, footer_style)
    elements.append(footer)
    
    # Build PDF
    doc.build(elements)
    print(f"✓ Invoice PDF generated successfully: {output_file}")
    print(f"✓ Total amount: €{total_cost:.2f}")
    print(f"✓ Number of items: {len(expense_data)}")


def main():
    """Main function to generate the invoice PDF."""
    import sys
    
    # Default values
    csv_file = 'data.csv'
    output_file = 'factura.pdf'
    logo_file = 'logo.png'
    
    # Check if custom CSV file is provided
    if len(sys.argv) > 1:
        csv_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    if len(sys.argv) > 3:
        logo_file = sys.argv[3]
    
    # Verify CSV file exists
    if not os.path.exists(csv_file):
        print(f"Error: CSV file '{csv_file}' not found.")
        print("Usage: python generate_invoice.py [csv_file] [output_pdf] [logo_file]")
        sys.exit(1)
    
    # Generate the invoice
    try:
        create_invoice_pdf(csv_file, output_file, logo_file)
    except Exception as e:
        print(f"Error generating invoice: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
