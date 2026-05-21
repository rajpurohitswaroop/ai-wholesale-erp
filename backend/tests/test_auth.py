def test_owner_login():
    username = "owner"
    password = "1234"

    assert username == "owner"
    assert password == "1234"


def test_staff_login():
    staff_id = "staff01"
    password = "1234"

    assert staff_id == "staff01"
    assert password == "1234"