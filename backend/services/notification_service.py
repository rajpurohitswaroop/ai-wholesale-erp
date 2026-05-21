def create_notification(title, message, notification_type="info"):
    return {
        "status": "success",
        "notification": {
            "title": title,
            "message": message,
            "type": notification_type
        }
    }


def send_low_stock_alert(product_name, stock):
    return create_notification(
        "Low Stock Alert",
        f"{product_name} ka stock low hai. Current stock: {stock}",
        "warning"
    )