def test_bill_total():
    items = [
        {"product": "Sugar", "qty": 10, "rate": 42},
        {"product": "Oil", "qty": 5, "rate": 1250}
    ]

    total = sum(item["qty"] * item["rate"] for item in items)

    assert total == 6670


def test_gst_calculation():
    amount = 1000
    gst = 5
    final_amount = amount + (amount * gst / 100)

    assert final_amount == 1050