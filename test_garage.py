from garage import get_available_spots

def test_available_spots_passing():
    garage = {
        "capacity": 10,
        "cars": {}
    }
    assert get_available_spots(garage) == 10


def test_available_spots_spot_taken():
    garage = {
        "capacity": 10,
        "cars": {"A", 1}
    }
    assert get_available_spots(garage) == 8

def test_available_spots_never_negative ():
    garage = {
        "capacity": 1,
        "cars": {"A", 1, "B", 2}
    }
    assert get_available_spots(garage) == 0