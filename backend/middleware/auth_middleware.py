from functools import wraps
from flask import request, jsonify


def require_role(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            role = request.headers.get("Role")

            if role != required_role:
                return jsonify({
                    "status": "error",
                    "message": "Access denied"
                }), 403

            return func(*args, **kwargs)

        return wrapper
    return decorator