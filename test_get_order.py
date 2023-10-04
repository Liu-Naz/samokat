import functions


def positive_assert():
    track_number = functions.get_new_track()
    assert functions.get_order(track_number).status_code == 200


def test_get_order():
    positive_assert()
