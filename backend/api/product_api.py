from flask import Blueprint, request, jsonify

product_api = Blueprint("product_api", __name__, url_prefix="/api/products")

products = []

@product_api.route("/", methods=["GET"])
def get_products():
    return jsonify({"status": "success", "products": products})

@product_api.route("/add", methods=["POST"])
def add_product():
    data = request.json or {}
    product = {
        "id": len(products) + 1,
        "name": data.get("name"),
       "price": data.get("price", 0),
        "stock": data.get("stock", 0),
        "category": data.get("category", "General")
    }
    products.append(product)
    return jsonify({"status": "success", "message": "Product added", "product": product})