from flask import Blueprint, request, jsonify

khata_api = Blueprint("khata_api", __name__, url_prefix="/api/khata")

khata_list = []

@khata_api.route("/", methods=["GET"])
def get_khata():
    return jsonify({
        "status": "success",
        "khata": khata_list
    })

@khata_api.route("/add", methods=["POST"])
def add_khata():
    data = request.json or {}

    khata = {
        "id": len(khata_list) + 1,
        "customer_name": data.get("customer_name"),
        "amount": data.get("amount", 0),
        "due_date": data.get("due_date", "")
    }

    khata_list.append(khata)

    return jsonify({
        "status": "success",
        "message": "Khata added successfully",
        "khata": khata
    })