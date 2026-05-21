def auto_detect_payment(transaction_id, expected_amount, received_amount):
    if not transaction_id:
        return {
            "status": "error",
            "message": "Transaction ID missing"
        }

    paid = float(expected_amount) == float(received_amount)

    return {
        "status": "success",
        "transaction_id": transaction_id,
        "expected_amount": expected_amount,
        "received_amount": received_amount,
        "payment_matched": paid,
        "message": "Payment auto detected" if paid else "Payment amount mismatch"
    }


def update_bill_payment_status(bill_id, payment_status="Paid"):
    return {
        "status": "success",
        "bill_id": bill_id,
        "payment_status": payment_status,
        "message": "Bill payment status updated"
    }