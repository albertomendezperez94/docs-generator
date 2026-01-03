#!/bin/bash

# Demo script to showcase the invoice generator capabilities

echo "=========================================="
echo "Invoice Generator Demo"
echo "=========================================="
echo ""

# Demo 1: Default invoice
echo "1. Generating default invoice (data.csv)..."
python generate_invoice.py
echo ""

# Demo 2: Custom invoice with example data
echo "2. Generating custom invoice (example_data.csv)..."
python generate_invoice.py example_data.csv custom_invoice.pdf
echo ""

# Demo 3: Display statistics
echo "=========================================="
echo "Generated Files:"
echo "=========================================="
if ls *.pdf >/dev/null 2>&1; then
    for file in *.pdf; do
        [ -e "$file" ] && ls -lh "$file" | awk '{print "  - " $9 " (" $5 ")"}'
    done
fi
echo ""

echo "=========================================="
echo "CSV Data Files:"
echo "=========================================="
if ls *.csv >/dev/null 2>&1; then
    for file in *.csv; do
        [ -e "$file" ] && ls -lh "$file" | awk '{print "  - " $9 " (" $5 ")"}'
    done
fi
echo ""

echo "=========================================="
echo "Demo Complete!"
echo "=========================================="
echo ""
echo "You can now open the PDF files to view the professional invoices:"
echo "  - factura.pdf (from data.csv)"
echo "  - custom_invoice.pdf (from example_data.csv)"
echo ""
