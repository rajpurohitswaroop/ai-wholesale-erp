def create_upi_payment(amount, upi_id, customer_name="Customer"):
    if not upi_id:
        return {
            "status": "error",
            "message": "UPI ID required"
        }

    return {
        "status": "success",
        "customer_name": customer_name,
        "amount": amount,
        "upi_id": upi_id,
        "payment_status": "Pending",
        "message": "UPI payment request created"
    }


def confirm_upi_payment(transaction_id, amount):
    return {
        "status": "success",
        "transaction_id": transaction_id,
        "amount": amount,
        "payment_status": "Paid",
        "message": "UPI payment confirmed"
    }