def analyze_buying_patterns(orders):
    product_count = {}

    for order in orders:
        for item in order.get("items", []):
            product = item.get("product", "Unknown")
            product_count[product] = product_count.get(product, 0) + item.get("qty", 0)

    return {
        "status": "success",
        "buying_patterns": product_count
    }