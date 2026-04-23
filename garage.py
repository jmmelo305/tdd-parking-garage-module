def enter_garage (garage, car_id, entry_hour):
    return garage ["cars"]["A123"] == 10

def exit_garage (garage, car_id):
    pass

def get_available_spots(garage):
    spots = garage["capacity"] - len(garage["cars"])
    return max(spots, 0)

def calculate_fee(hours,rate):
    pass
