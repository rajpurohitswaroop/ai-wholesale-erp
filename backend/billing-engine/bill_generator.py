from gst_calculator import calculate_item_total


def generate_bill(customer_name, items, payment_status="Pending"):
    bill_items = []
    grand_total = 0

    for item in items:
        item_total = calculate_item_total(
            item.get("qty", 0),
            item.get("rate", 0),
            item.get("gst", 5)
        )

        bill_items.append({
            "product": item.get("product"),
            **item_total
        })

        grand_total += item_total["final_amount"]

    return {
        "status": "success",
        "customer_name": customer_name,
        "items": bill_items,
        "grand_total": round(grand_total, 2),
        "payment_status": payment_status,
        "message": "Bill generated successfully"
    }