def test_add_product():
    product = {
        "name": "Sugar 50kg",
        "rate": 2100,
        "stock": 100
    }

    assert product["name"] == "Sugar 50kg"
    assert product["rate"] == 2100
    assert product["stock"] == 100


def test_duplicate_product():
    products = ["Sugar 50kg", "Oil Tin", "Rice Bag"]
    new_product = "Sugar 50kg"

    assert new_product in products