def print_thermal_bill(bill_data):
    lines = []
    lines.append("AI WHOLESALE ERP")
    lines.append("--------------------")
    lines.append(f"Customer: {bill_data.get('customer_name')}")
    lines.append("--------------------")

    for item in bill_data.get("items", []):
        lines.append(
            f"{item.get('product')} x {item.get('qty')} = ₹{item.get('final_amount')}"
        )

    lines.append("--------------------")
    lines.append(f"Total: ₹{bill_data.get('grand_total')}")
    lines.append(f"Status: {bill_data.get('payment_status')}")
    lines.append("--------------------")

    return {
        "status": "success",
        "print_text": "\n".join(lines),
        "message": "Thermal bill print text generated"
    }