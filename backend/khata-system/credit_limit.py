def check_credit_limit(customer_name, current_pending, credit_limit):
    remaining_limit = credit_limit - current_pending

    return {
        "status": "success",
        "customer_name": customer_name,
        "credit_limit": credit_limit,
        "current_pending": current_pending,
        "remaining_limit": remaining_limit,
        "order_allowed": current_pending < credit_limit,
        "message": "Order allowed" if current_pending < credit_limit else "Credit limit exceeded"
    }


def update_credit_limit(customer_name, new_limit):
    return {
        "status": "success",
        "customer_name": customer_name,
        "new_credit_limit": new_limit,
        "message": "Credit limit updated successfully"
    }