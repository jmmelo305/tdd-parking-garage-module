from garage import enter_garage

def test_enter_garage_passing():
    garage = {
        "capacity": 10,
        "cars": {}
    }
    assert enter_garage(garage) == 15
