def success_response(message="Success", data=None):
    return {
        "status": "success",
        "message": message,
        "data": data
    }


def error_response(message="Something went wrong", code=400):
    return {
        "status": "error",
        "code": code,
        "message": message
    }