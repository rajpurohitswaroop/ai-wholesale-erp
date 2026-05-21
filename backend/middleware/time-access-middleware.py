from datetime import datetime


def is_time_access_allowed(open_time="08:00", close_time="20:00"):
    now = datetime.now().strftime("%H:%M")

    return {
        "status": "success",
        "allowed": open_time <= now <= close_time,
        "current_time": now,
        "open_time": open_time,
        "close_time": close_time
    }