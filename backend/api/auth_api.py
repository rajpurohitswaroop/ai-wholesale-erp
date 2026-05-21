from flask import Blueprint, request, jsonify

auth_api = Blueprint("auth_api", __name__, url_prefix="/api/auth")

@auth_api.route("/owner-login", methods=["POST"])
def owner_login():
    data = request.json or {}
    if data.get("username") == "owner" and data.get("password") == "1234":
        return jsonify({"status": "success", "role": "owner", "message": "Owner login successful"})
    return jsonify({"status": "error", "message": "Invalid owner login"}), 401

@auth_api.route("/staff-login", methods=["POST"])
def staff_login():
    data = request.json or {}
    if data.get("staff_id") == "staff01" and data.get("password") == "1234":
        return jsonify({"status": "success", "role": "staff", "message": "Staff login successful"})
    return jsonify({"status": "error", "message": "Invalid staff login"}), 401