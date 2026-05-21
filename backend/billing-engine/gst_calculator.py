def calculate_gst(amount, gst_percent=5):
    gst_amount = (amount * gst_percent) / 100
    final_amount = amount + gst_amount

    return {
        "amount": amount,
        "gst_percent": gst_percent,
        "gst_amount": round(gst_amount, 2),
        "final_amount": round(final_amount, 2)
    }


def calculate_item_total(qty, rate, gst_percent=5):
    base_total = qty * rate
    gst_data = calculate_gst(base_total, gst_percent)

    return {
        "qty": qty,
        "rate": rate,
        "base_total": base_total,
        "gst_amount": gst_data["gst_amount"],
        "final_amount": gst_data["final_amount"]
    }