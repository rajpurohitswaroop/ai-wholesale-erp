def get_product_list(products):
    return {
        "status": "success",
        "total_products": len(products),
        "products": products
    }


def search_product(products, keyword):
    result = [
        product for product in products
        if keyword.lower() in product.get("name", "").lower()
    ]

    return {
        "status": "success",
        "results": result
    }