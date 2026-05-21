def receive_whatsapp_order(customer_phone, message):
    if not customer_phone or not message:
        return {
            "status": "error",
            "message": "Customer phone and order message required"
        }

    return {
        "status": "success",
        "customer_phone": customer_phone,
        "order_message": message,
        "order_status": "received",
        "message": "WhatsApp order received successfully"
    }


def confirm_whatsapp_order(customer_phone, order_id):
    return {
        "status": "success",
        "customer_phone": customer_phone,
        "order_id": order_id,
        "confirmation_message": f"Aapka WhatsApp order #{order_id} confirm ho gaya hai ✅"
    }