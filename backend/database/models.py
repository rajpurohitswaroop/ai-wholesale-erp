def product_model(name, category="General", rate=0, stock=0, gst=5):
    return {
        "name": name,
        "category": category,
        "rate": rate,
        "stock": stock,
        "gst": gst
    }


def customer_model(name, phone="", khata_balance=0, credit_limit=0):
    return {
        "name": name,
        "phone": phone,
        "khata_balance": khata_balance,
        "credit_limit": credit_limit
    }


def bill_model(customer_name, total, payment_status="Pending"):
    return {
        "customer_name": customer_name,
        "total": total,
        "payment_status": payment_status
    }