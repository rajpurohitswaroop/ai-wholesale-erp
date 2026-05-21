def add_pending_payment(customer_name, amount, due_date=""):
    return {
        "status": "success",
        "customer_name": customer_name,
        "pending_amount": amount,
        "due_date": due_date,
        "message": "Pending payment added successfully"
    }


def get_pending_payments(payments):
    pending = [
        payment for payment in payments
        if payment.get("status", "Pending") == "Pending"
    ]

    return {
        "status": "success",
        "pending_payments": pending,
        "total_pending": sum(p.get("amount", 0) for p in pending)
    }