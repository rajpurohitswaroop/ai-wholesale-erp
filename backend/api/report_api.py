from flask import Blueprint, jsonify

report_api = Blueprint("report_api", __name__, url_prefix="/api/reports")

@report_api.route("/daily", methods=["GET"])
def daily_report():
    return jsonify({"status": "success", "sales": 45000, "profit": 8500, "pending": 12000})

@report_api.route("/monthly", methods=["GET"])
def monthly_report():
    return jsonify({"status": "success", "sales": 920000, "profit": 165000, "pending": 88000})