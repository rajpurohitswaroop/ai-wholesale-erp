def owner_login(username, password):
    if username == "owner" and password == "1234":
        return {
            "status": "success",
            "role": "owner",
            "message": "Owner login successful"
        }

    return {
        "status": "error",
        "message": "Invalid owner username or password"
    }