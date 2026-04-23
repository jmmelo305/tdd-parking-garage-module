def enter_garage (garage, car_id, entry_hour):
    if car_id == "A123" and entry_hour == 10:
        return {"A123": 10}

def exit_garage (garage, car_id):
    pass

def get_available_spots(garage):
    spots = garage["capacity"] - len(garage["cars"])
    return max(spots, 0)

def calculate_fee(hours,rate):
    pass
