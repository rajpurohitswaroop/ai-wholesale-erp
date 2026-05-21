from flask import Blueprint, request, jsonify

stock_api = Blueprint("stock_api", __name__, url_prefix="/api/stock")

@stock_api.route("/update", methods=["POST"])
def update_stock():
    data = request.json or {}
    return jsonify({
        "status": "success",
        "message": "Stock updated",
        "product": data.get("product"),
        "quantity": data.get("quantity")
    })

@stock_api.route("/low-alerts", methods=["GET"])
def low_stock_alerts():
    return jsonify({
        "status": "success",
        "alerts": ["Sugar stock low", "Oil stock low"]
    })