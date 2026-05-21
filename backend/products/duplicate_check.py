def check_duplicate_product(products, product_name):
    exists = any(
        product.get("name", "").lower() == product_name.lower()
        for product in products
    )

    return {
        "status": "success",
        "product_name": product_name,
        "duplicate": exists,
        "message": "Duplicate found" if exists else "No duplicate found"
    }