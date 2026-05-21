def send_whatsapp_message(phone, message):
    if not phone:
        return {
            "status": "error",
            "message": "Phone number required"
        }

    return {
        "status": "success",
        "phone": phone,
        "message": message,
        "sent": True
    }


def send_order_confirmation(phone, order_id):
    return send_whatsapp_message(
        phone,
        f"Aapka order #{order_id} confirm ho gaya hai ✅"
    )