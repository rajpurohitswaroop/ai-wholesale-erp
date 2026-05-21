def expense_category_summary(expenses):
    summary = {}

    for expense in expenses:
        category = expense.get("category", "General")
        summary[category] = summary.get(category, 0) + expense.get("amount", 0)

    return {
        "status": "success",
        "category_summary": summary
    }


def highest_expense(expenses):
    if not expenses:
        return {
            "status": "success",
            "highest_expense": None
        }

    return {
        "status": "success",
        "highest_expense": max(expenses, key=lambda x: x.get("amount", 0))
    }