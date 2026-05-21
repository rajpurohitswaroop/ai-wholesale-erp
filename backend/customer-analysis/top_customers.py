def get_top_customers(customers):
    sorted_customers = sorted(
        customers,
        key=lambda x: x.get("total_purchase", 0),
        reverse=True
    )

    return {
        "status": "success",
        "top_customers": sorted_customers[:10]
    }