def add_product(name, category="General", rate=0, stock=0, gst=5):
    if not name:
        return {
            "status": "error",
            "message": "Product name required"
        }

    return {
        "status": "success",
        "product": {
            "name": name,
            "category": category,
            "rate": rate,
            "stock": stock,
            "gst": gst
        },
        "message": "Product added successfully"
    }