def generate_payment_receipt(customer_name, amount, method="UPI", transaction_id=""):
    return {
        "status": "success",
        "receipt": {
            "customer_name": customer_name,
            "amount": amount,
            "method": method,
            "transaction_id": transaction_id,
            "payment_status": "Paid"
        },
        "message": "Payment receipt generated successfully"
    }


def send_whatsapp_receipt(customer_phone, receipt_data):
    return {
        "status": "success",
        "customer_phone": customer_phone,
        "receipt_data": receipt_data,
        "message": "WhatsApp receipt sent successfully"
    }