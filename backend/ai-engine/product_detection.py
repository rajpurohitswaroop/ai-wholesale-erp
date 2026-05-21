def detect_product_from_text(order_text):
    products = ["sugar", "oil", "rice", "tea", "soap"]

    detected = []

    for product in products:
        if product.lower() in order_text.lower():
            detected.append(product)

    return {
        "status": "success",
        "detected_products": detected
    }


def detect_quantity(order_text):
    words = order_text.split()
    quantities = []

    for word in words:
        if word.isdigit():
            quantities.append(int(word))

    return {
        "status": "success",
        "quantities": quantities
    }