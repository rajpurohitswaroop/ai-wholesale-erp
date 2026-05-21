def analyze_late_payments(customers):
    late_customers = []

    for customer in customers:
        if customer.get("due_days", 0) > 7:
            late_customers.append(customer)

    return {
        "status": "success",
        "late_payment_customers": late_customers,
        "total_late_customers": len(late_customers)
    }