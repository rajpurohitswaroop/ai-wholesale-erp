from flask import Blueprint, request, jsonify

whatsapp_api = Blueprint("whatsapp_api", __name__, url_prefix="/api/whatsapp")

@whatsapp_api.route("/order", methods=["POST"])
def whatsapp_order():
    data = request.json or {}
    return jsonify({"status": "success", "message": "WhatsApp order received", "order": data})

@whatsapp_api.route("/auto-reply", methods=["POST"])
def auto_reply():
    return jsonify({"status": "success", "reply": "Namaste, aapka order receive ho gaya hai ✅"})