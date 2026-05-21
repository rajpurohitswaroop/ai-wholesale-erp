from flask import Blueprint, request, jsonify

timing_api = Blueprint("timing_api", __name__, url_prefix="/api/timing")

business_timing = {
    "open_time": "08:00",
    "close_time": "20:00",
    "status": "open"
}

@timing_api.route("/settings", methods=["GET"])
def get_timing():
    return jsonify({"status": "success", "timing": business_timing})

@timing_api.route("/settings", methods=["POST"])
def update_timing():
    data = request.json or {}
    business_timing["open_time"] = data.get("open_time", business_timing["open_time"])
    business_timing["close_time"] = data.get("close_time", business_timing["close_time"])
    business_timing["status"] = data.get("status", business_timing["status"])
    return jsonify({"status": "success", "message": "Timing updated", "timing": business_timing})