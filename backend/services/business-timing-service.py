from datetime import datetime


def is_business_open(open_time="08:00", close_time="20:00"):
    current_time = datetime.now().strftime("%H:%M")
    is_open = open_time <= current_time <= close_time

    return {
        "status": "success",
        "business_open": is_open,
        "current_time": current_time,
        "open_time": open_time,
        "close_time": close_time,
        "message": "Business is OPEN" if is_open else "Business is CLOSED"
    }


def shop_closed_reply(open_time="08:00"):
    return {
        "status": "success",
        "reply": f"Shop abhi closed hai. Hum subah {open_time} baje open honge."
    }