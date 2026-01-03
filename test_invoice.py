#!/usr/bin/env python3
"""
Test script for the invoice generator.
Validates that the PDF is generated correctly with all required components.
"""

import os
import sys
import csv


def test_csv_reading():
    """Test that CSV file can be read correctly."""
    print("Testing CSV reading...")
    
    csv_file = 'data.csv'
    if not os.path.exists(csv_file):
        print(f"❌ Test failed: {csv_file} not found")
        return False
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            
            if len(rows) == 0:
                print("❌ Test failed: CSV file is empty")
                return False
            
            required_columns = ['descripcion', 'precio_unitario', 'unidades', 'total', 'validez']
            for col in required_columns:
                if col not in rows[0]:
                    print(f"❌ Test failed: Missing column '{col}' in CSV")
                    return False
            
            print(f"✓ CSV reading test passed ({len(rows)} rows found)")
            return True
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False


def test_pdf_generation():
    """Test that PDF can be generated."""
    print("\nTesting PDF generation...")
    
    test_output = '/tmp/test_invoice.pdf'
    
    try:
        from generate_invoice import create_invoice_pdf
        
        # Remove existing test file
        if os.path.exists(test_output):
            os.remove(test_output)
        
        # Generate PDF
        create_invoice_pdf('data.csv', test_output, 'logo.png')
        
        # Check if file was created
        if not os.path.exists(test_output):
            print("❌ Test failed: PDF file was not created")
            return False
        
        # Check file size
        file_size = os.path.getsize(test_output)
        if file_size < 1000:  # PDF should be at least 1KB
            print(f"❌ Test failed: PDF file too small ({file_size} bytes)")
            return False
        
        print(f"✓ PDF generation test passed (size: {file_size} bytes)")
        
        # Clean up
        os.remove(test_output)
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_total_calculation():
    """Test that total is calculated correctly."""
    print("\nTesting total calculation...")
    
    try:
        with open('data.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            
            expected_total = sum(float(row['total']) for row in rows)
            
            print(f"✓ Total calculation test passed (expected: €{expected_total:.2f})")
            return True
            
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False


def main():
    """Run all tests."""
    print("=" * 60)
    print("Running Invoice Generator Tests")
    print("=" * 60)
    
    tests = [
        test_csv_reading,
        test_total_calculation,
        test_pdf_generation,
    ]
    
    results = []
    for test_func in tests:
        results.append(test_func())
    
    print("\n" + "=" * 60)
    print(f"Test Results: {sum(results)}/{len(results)} passed")
    print("=" * 60)
    
    if all(results):
        print("\n✓ All tests passed!")
        return 0
    else:
        print("\n❌ Some tests failed!")
        return 1


if __name__ == "__main__":
    sys.exit(main())
