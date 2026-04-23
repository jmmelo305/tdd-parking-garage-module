from garage import get_available_spots

def test_available_spots_passing():
    garage = {
        "capacity": 10,
        "cars": {}
    }
    assert available_spots(garage) == 15
