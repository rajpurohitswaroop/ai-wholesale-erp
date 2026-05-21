from datetime import datetime


def create_stock_history(product_name, old_stock, new_stock, action="update"):
    return {
        "status": "success",
        "history": {
            "product_name": product_name,
            "old_stock": old_stock,
            "new_stock": new_stock,
            "action": action,
            "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        "message": "Stock history created successfully"
    }


def get_stock_history(history_list):
    return {
        "status": "success",
        "history": history_list
    }