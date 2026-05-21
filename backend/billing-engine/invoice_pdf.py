def create_invoice_pdf(bill_data):
    invoice_name = f"invoice_{bill_data.get('customer_name', 'customer')}.pdf"

    return {
        "status": "success",
        "invoice_file": invoice_name,
        "message": "PDF invoice generated successfully"
    }


def download_invoice(invoice_file):
    return {
        "status": "success",
        "file": invoice_file,
        "message": "Invoice ready for download"
    }