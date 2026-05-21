def calculate_profit(total_sales, total_expenses):
    profit = total_sales - total_expenses

    return {
        "status": "success",
        "total_sales": total_sales,
        "total_expenses": total_expenses,
        "profit": profit,
        "message": "Profit report generated successfully"
    }