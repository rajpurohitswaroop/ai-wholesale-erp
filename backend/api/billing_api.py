from flask import Blueprint, request, jsonify

billing_api = Blueprint("billing_api", __name__, url_prefix="/api/billing")

@billing_api.route("/create", methods=["POST"])
def create_bill():
    data = request.json or {}
    items = data.get("items", [])
    total = sum(item.get("qty", 0) * item.get("rate", 0) for item in items)

    return jsonify({
        "status": "success",
        "message": "Bill generated",
        "customer": data.get("customer"),
        "total": total,
        "payment_status": data.get("payment_status", "Pending")
    })