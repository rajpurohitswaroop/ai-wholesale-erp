def check_low_stock(products, limit=10):
    low_stock_products = [
        product for product in products
        if product.get("stock", 0) <= limit
    ]

    return {
        "status": "success",
        "limit": limit,
        "low_stock_products": low_stock_products,
        "total_alerts": len(low_stock_products)
    }