from datetime import datetime, time


def is_billing_allowed(open_time="08:00", close_time="20:00"):
    now = datetime.now().time()

    open_hour, open_minute = map(int, open_time.split(":"))
    close_hour, close_minute = map(int, close_time.split(":"))

    start = time(open_hour, open_minute)
    end = time(close_hour, close_minute)

    allowed = start <= now <= end

    return {
        "status": "success",
        "billing_allowed": allowed,
        "open_time": open_time,
        "close_time": close_time,
        "message": "Billing ON" if allowed else "Billing OFF after closing"
    }