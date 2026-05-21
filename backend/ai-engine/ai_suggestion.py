def get_ai_suggestions():
    return {
        "status": "success",
        "suggestions": [
            "Sugar stock low hai, reorder karo",
            "Oil product fast selling hai",
            "Top customer ko special rate do"
        ]
    }


def smart_recommendation(product_name):
    return {
        "product": product_name,
        "recommendation": f"{product_name} ke liye demand high ho sakti hai"
    }