import functions


def positive_assert():
    assert functions.get_order().status_code == 200


def test_get_order():
    positive_assert()
