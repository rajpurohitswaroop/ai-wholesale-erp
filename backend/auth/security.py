import hashlib


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password, hashed_password):
    return hash_password(password) == hashed_password


def create_session(user_id, role):
    return {
        "status": "active",
        "user_id": user_id,
        "role": role
    }