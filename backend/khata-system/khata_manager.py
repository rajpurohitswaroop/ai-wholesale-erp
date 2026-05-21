def create_khata_entry(customer_name, bill_amount, paid_amount=0):
    pending_amount = bill_amount - paid_amount

    return {
        "status": "success",
        "customer_name": customer_name,
        "bill_amount": bill_amount,
        "paid_amount": paid_amount,
        "pending_amount": pending_amount,
        "message": "Khata entry created successfully"
    }


def khata_summary(entries):
    total_bill = sum(entry.get("bill_amount", 0) for entry in entries)
    total_paid = sum(entry.get("paid_amount", 0) for entry in entries)
    total_pending = total_bill - total_paid

    return {
        "status": "success",
        "total_bill": total_bill,
        "total_paid": total_paid,
        "total_pending": total_pending
    }