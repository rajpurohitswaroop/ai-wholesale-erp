from db import get_db_connection, init_db


def seed_products():
    init_db()

    conn = get_db_connection()
    cursor = conn.cursor()

    sample_products = [
        ("Sugar 50kg", "Grocery", 2100, 100, 5),
        ("Oil Tin", "Oil", 1250, 50, 5),
        ("Rice Bag", "Grain", 1800, 80, 5)
    ]

    cursor.executemany("""
    INSERT INTO products (name, category, rate, stock, gst)
    VALUES (?, ?, ?, ?, ?)
    """, sample_products)

    conn.commit()
    conn.close()

    return {
        "status": "success",
        "message": "Sample products added successfully"
    }