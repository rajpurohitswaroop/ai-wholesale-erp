def generate_qr_payment(amount, upi_id="", customer_name="Customer"):
    return {
        "status": "success",
        "customer_name": customer_name,
        "amount": amount,
        "upi_id": upi_id,
        "qr_status": "generated",
        "message": "QR payment generated successfully"
    }


def verify_qr_payment(transaction_id, amount):
    if not transaction_id:
        return {
            "status": "error",
            "message": "Transaction ID required"
        }

    return {
        "status": "success",
        "transaction_id": transaction_id,
        "amount": amount,
        "verified": True,
        "message": "QR payment verified successfully"
    }