def forecast_sales(product_name, current_sales):
    predicted_sales = current_sales + int(current_sales * 0.20)

    return {
        "status": "success",
        "product": product_name,
        "current_sales": current_sales,
        "predicted_sales": predicted_sales,
        "message": "AI forecast generated"
    }


def fast_selling_analysis(products):
    sorted_products = sorted(
        products,
        key=lambda x: x.get("sales", 0),
        reverse=True
    )

    return {
        "status": "success",
        "fast_selling_products": sorted_products[:5]
    }