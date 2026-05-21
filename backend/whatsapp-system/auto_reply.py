def send_auto_reply(customer_phone, customer_message):
    if not customer_phone:
        return {
            "status": "error",
            "message": "Customer phone required"
        }

    reply = "Namaste 🙏 Aapka message receive ho gaya hai. Hum jaldi reply karenge."

    if "rate" in customer_message.lower():
        reply = "Rate inquiry receive ho gayi hai. Product ka naam bhejiye."
    elif "order" in customer_message.lower():
        reply = "Order receive ho gaya hai. Confirmation ke liye wait karein."

    return {
        "status": "success",
        "customer_phone": customer_phone,
        "reply": reply
    }