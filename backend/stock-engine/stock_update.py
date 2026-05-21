def update_stock(product, quantity, action="add"):
    if not product:
        return {
            "status": "error",
            "message": "Product not found"
        }

    current_stock = product.get("stock", 0)

    if action == "add":
        product["stock"] = current_stock + quantity
    elif action == "deduct":
        product["stock"] = max(current_stock - quantity, 0)
    else:
        return {
            "status": "error",
            "message": "Invalid stock action"
        }

    return {
        "status": "success",
        "product": product,
        "message": "Stock updated successfully"
    }


def auto_stock_deduction(product, sold_quantity):
    return update_stock(product, sold_quantity, "deduct")