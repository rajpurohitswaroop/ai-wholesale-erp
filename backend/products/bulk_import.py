def bulk_import_products(product_rows):
    imported = []

    for row in product_rows:
        imported.append({
            "name": row.get("name"),
            "category": row.get("category", "General"),
            "rate": row.get("rate", 0),
            "stock": row.get("stock", 0),
            "gst": row.get("gst", 5)
        })

    return {
        "status": "success",
        "imported_count": len(imported),
        "products": imported,
        "message": "Bulk products imported successfully"
    }