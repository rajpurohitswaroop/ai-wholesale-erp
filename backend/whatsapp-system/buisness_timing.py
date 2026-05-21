from datetime import datetime


def is_whatsapp_order_allowed(open_time="08:00", close_time="20:00"):
    current_time = datetime.now().strftime("%H:%M")
    allowed = open_time <= current_time <= close_time

    return {
        "status": "success",
        "allowed": allowed,
        "current_time": current_time,
        "open_time": open_time,
        "close_time": close_time,
        "message": "Order allowed" if allowed else "Shop closed"
    }


def shop_closed_auto_reply(open_time="08:00"):
    return {
        "status": "success",
        "reply": f"Shop abhi closed hai. Order subah {open_time} ke baad accept hoga."
    }