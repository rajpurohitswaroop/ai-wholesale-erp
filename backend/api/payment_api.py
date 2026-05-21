from flask import Blueprint, request, jsonify

payment_api = Blueprint("payment_api", __name__, url_prefix="/api/payment")

@payment_api.route("/confirm", methods=["POST"])
def confirm_payment():
    data = request.json or {}
    return jsonify({
        "status": "success",
        "message": "Payment confirmed",
        "amount": data.get("amount"),
        "method": data.get("method", "UPI")
    })

@payment_api.route("/receipt", methods=["POST"])
def payment_receipt():
    data = request.json or {}
    return jsonify({"status": "success", "message": "Receipt generated", "data": data})