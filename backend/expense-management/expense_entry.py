def add_expense(title, amount, category="General", added_by="Staff"):
    if not title or amount <= 0:
        return {
            "status": "error",
            "message": "Valid expense title and amount required"
        }

    return {
        "status": "success",
        "expense": {
            "title": title,
            "amount": amount,
            "category": category,
            "added_by": added_by
        },
        "message": "Expense added successfully"
    }