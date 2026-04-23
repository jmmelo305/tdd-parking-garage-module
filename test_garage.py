import pytest
from garage import get_available_spots, enter_garage, exit_garage
# enter_garage
def test_enter_garage_A123_at_10():
    garage = {
        "capacity": 10,
        "cars": {}
    }

    result = enter_garage(garage, "A123", 10)
    assert garage["cars"] == {"A123": 10}
    assert result is None

def test_enter_garage_duplicate_value_error():
    garage = {
        "capacity": 10,
        "cars": {"A123": 10}
    }
    with pytest.raises(ValueError):
        enter_garage(garage, "A123", 11)

# get_available_spots
def test_get_available_spots_passing():
    garage = {
        "capacity": 10,
        "cars": {}
    }
    assert get_available_spots(garage) == 10

def test_get_available_spots_spot_taken():
    garage = {
        "capacity": 10,
        "cars": {"A", 1}
    }
    assert get_available_spots(garage) == 8

def test_get_available_spots_never_negative ():
    garage = {
        "capacity": 1,
        "cars": {"A", 1, "B", 2}
    }
    assert get_available_spots(garage) == 0


# exit_garage

def test_exit_garage_A123_capacity_10():
    garage = {
        "capacity": 10,
        "cars": {"A123": 10}
    }
    assert garage["cars"] == {}
    assert result is None