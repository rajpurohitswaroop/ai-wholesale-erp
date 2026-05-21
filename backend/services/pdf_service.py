def create_pdf_file(file_name, content):
    return {
        "status": "success",
        "file_name": file_name,
        "content": content,
        "message": "PDF file data prepared successfully"
    }


def create_invoice_pdf_data(customer_name, total_amount):
    return create_pdf_file(
        f"invoice_{customer_name}.pdf",
        {
            "customer_name": customer_name,
            "total_amount": total_amount
        }
    )