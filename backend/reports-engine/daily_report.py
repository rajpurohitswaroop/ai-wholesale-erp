def generate_daily_report(sales, expenses, pending_payments):
    total_sales = sum(item.get("amount", 0) for item in sales)
    total_expenses = sum(item.get("amount", 0) for item in expenses)
    total_pending = sum(item.get("amount", 0) for item in pending_payments)

    profit = total_sales - total_expenses

    return {
        "status": "success",
        "report_type": "daily",
        "total_sales": total_sales,
        "total_expenses": total_expenses,
        "total_pending": total_pending,
        "profit": profit
    }