def get_stock_summary(products):
    total_products = len(products)
    total_stock = sum(product.get("stock", 0) for product in products)

    return {
        "status": "success",
        "total_products": total_products,
        "total_stock": total_stock,
        "products": products
    }


def search_stock(products, keyword):
    result = [
        product for product in products
        if keyword.lower() in product.get("name", "").lower()
    ]

    return {
        "status": "success",
        "results": result
    }