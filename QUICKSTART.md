# 🚀 Quick Start Guide

Get started with the Professional Invoice PDF Generator in just 3 steps!

## Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

## Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

## Step 2: Generate Your First Invoice
```bash
python generate_invoice.py
```

That's it! You'll see:
```
Created placeholder logo: logo.png
✓ Invoice PDF generated successfully: factura.pdf
✓ Total amount: €9345.00
✓ Number of items: 5
```

## Step 3: View Your Invoice
Open `factura.pdf` with any PDF viewer.

---

## Using Your Own Data

### 1. Create a CSV file
Create a file named `my_data.csv` with this structure:
```csv
descripcion,precio_unitario,unidades,total,validez
Service Name,100.00,10,1000.00,30 días
Another Service,50.00,5,250.00,15 días
```

### 2. Generate the invoice
```bash
python generate_invoice.py my_data.csv my_invoice.pdf
```

### 3. Open `my_invoice.pdf`
Your professional invoice is ready!

---

## Using Your Own Logo

### 1. Prepare your logo
- Format: PNG or JPG
- Recommended size: 200x80 pixels (or similar ratio)
- Save it as `company_logo.png`

### 2. Generate with custom logo
```bash
python generate_invoice.py data.csv invoice.pdf company_logo.png
```

---

## Run Tests
Verify everything works:
```bash
python test_invoice.py
```

---

## Run Demo
See multiple examples:
```bash
bash demo.sh
```

---

## Need Help?

- **Full Documentation**: See [README.md](README.md)
- **PDF Structure**: See [ESTRUCTURA_PDF.md](ESTRUCTURA_PDF.md)
- **Visual Preview**: See [VISUAL_PREVIEW.md](VISUAL_PREVIEW.md)
- **Implementation Details**: See [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)

---

## Common Issues

### "Module not found" error
```bash
pip install -r requirements.txt
```

### "CSV file not found" error
Make sure the CSV file exists in the current directory or provide the full path:
```bash
python generate_invoice.py /full/path/to/data.csv
```

### Logo doesn't appear
- Check the image file exists
- Supported formats: PNG, JPG, GIF
- If no logo is provided, a placeholder will be created automatically

---

## What's Next?

1. **Customize colors**: Edit the color hex codes in `generate_invoice.py`
2. **Change fonts**: Modify the font names and sizes in the script
3. **Add more data**: Include additional rows in your CSV file
4. **Translate**: Change text strings to your preferred language

---

## Example Output

The generated PDF includes:
- ✓ Professional header with logo
- ✓ "FACTURA" title
- ✓ Automatic date
- ✓ Complete expense table
- ✓ Highlighted total (in red)
- ✓ Professional footer with details

**Sample file**: `factura.pdf` (generated from `data.csv`)
**Total**: €9,345.00
**Items**: 5 services

---

## Support

For questions or issues, please refer to the documentation files or create an issue in the repository.

**Happy invoicing! 🎉**
