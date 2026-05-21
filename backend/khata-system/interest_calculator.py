def calculate_late_interest(amount, due_days, interest_percent=2):
    if due_days <= 0:
        interest = 0
    else:
        interest = (amount * interest_percent * due_days) / 100

    total_amount = amount + interest

    return {
        "status": "success",
        "pending_amount": amount,
        "due_days": due_days,
        "interest_percent": interest_percent,
        "interest_amount": round(interest, 2),
        "total_amount": round(total_amount, 2)
    }


def interest_on_off(enabled=True):
    return {
        "status": "success",
        "interest_enabled": enabled,
        "message": "Interest ON" if enabled else "Interest OFF"
    }