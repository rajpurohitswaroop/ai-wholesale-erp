def daily_expense_report(expenses):
    total = sum(expense.get("amount", 0) for expense in expenses)

    return {
        "status": "success",
        "total_expense": total,
        "expenses": expenses
    }


def monthly_expense_report(expenses):
    total = sum(expense.get("amount", 0) for expense in expenses)

    return {
        "status": "success",
        "monthly_total_expense": total,
        "expense_count": len(expenses),
        "expenses": expenses
    }