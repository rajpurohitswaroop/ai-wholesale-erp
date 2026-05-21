def customer_loyalty_score(customer):
    purchase = customer.get("total_purchase", 0)
    orders = customer.get("total_orders", 0)
    payment_score = customer.get("payment_score", 0)

    score = (purchase / 1000) + (orders * 2) + payment_score

    return {
        "status": "success",
        "customer": customer.get("name"),
        "loyalty_score": round(score, 2)
    }


def analyze_loyal_customers(customers):
    scored = [customer_loyalty_score(c) for c in customers]

    return {
        "status": "success",
        "loyal_customers": sorted(
            scored,
            key=lambda x: x["loyalty_score"],
            reverse=True
        )
    }