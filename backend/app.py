from flask import Flask, jsonify
from flask_cors import CORS
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "AI Wholesale ERP Backend Running Successfully 🚀"
    })


@app.route("/health")
def health_check():
    return jsonify({
        "status": "ok",
        "backend": "active",
        "system": "AI Wholesale ERP"
    })


# Safe blueprint register function
def register_blueprint_safe(import_path, blueprint_name):
    try:
        module = __import__(import_path, fromlist=[blueprint_name])
        blueprint = getattr(module, blueprint_name)
        app.register_blueprint(blueprint)
        print(f"✅ Loaded: {import_path}")
    except Exception as e:
        print(f"⚠ Skipped {import_path}: {e}")


# API routes
register_blueprint_safe("api.auth_api", "auth_api")
register_blueprint_safe("api.product_api", "product_api")
register_blueprint_safe("api.billing_api", "billing_api")
register_blueprint_safe("api.stock_api", "stock_api")
register_blueprint_safe("api.khata_api", "khata_api")
register_blueprint_safe("api.payment_api", "payment_api")
register_blueprint_safe("api.report_api", "report_api")
register_blueprint_safe("api.whatsapp_api", "whatsapp_api")
register_blueprint_safe("api.timing_api", "timing_api")


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "status": "error",
        "message": "API route not found"
    }), 404


@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "status": "error",
        "message": "Internal server error"
    }), 500


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )