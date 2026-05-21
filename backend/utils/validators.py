def is_required(value):
    return value is not None and str(value).strip() != ""


def validate_amount(amount):
    try:
        return float(amount) > 0
    except (TypeError, ValueError):
        return False


def validate_phone(phone):
    phone = str(phone).strip()
    return phone.isdigit() and len(phone) == 10