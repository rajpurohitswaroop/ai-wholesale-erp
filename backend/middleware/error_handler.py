def handle_error(error_message, code=500):
    return {
        "status": "error",
        "code": code,
        "message": error_message
    }


def handle_success(message, data=None):
    return {
        "status": "success",
        "message": message,
        "data": data
    }