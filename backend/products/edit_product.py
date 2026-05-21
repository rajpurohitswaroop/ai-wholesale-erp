def edit_product(product, updates):
    if not product:
        return {
            "status": "error",
            "message": "Product not found"
        }

    product.update(updates)

    return {
        "status": "success",
        "product": product,
        "message": "Product updated successfully"
    }