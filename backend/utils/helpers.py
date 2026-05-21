from datetime import datetime


def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def generate_id(prefix="ERP"):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{prefix}-{timestamp}"


def calculate_percentage(amount, percent):
    return round((amount * percent) / 100, 2)