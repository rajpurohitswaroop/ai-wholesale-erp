def staff_login(staff_id, password):
    if staff_id == "staff01" and password == "1234":
        return {
            "status": "success",
            "role": "staff",
            "permissions": ["billing", "stock_view", "expense_entry"],
            "message": "Staff login successful"
        }

    return {
        "status": "error",
        "message": "Invalid staff ID or password"
    }