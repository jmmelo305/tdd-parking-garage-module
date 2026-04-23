def enter_garage (garage, car_id, entry_hour):
    if garage ["capacity"] == 10 and car_id == "A123" and car_id in garage ["cars"]:
        raise ValueError
    
    if garage ["capacity"] == 10 and car_id == "A123" and entry_hour == 10:
        garage ["cars"] = {"A123": 10}
    return None

    

def exit_garage (garage, car_id):
    pass

def get_available_spots(garage):
    spots = garage["capacity"] - len(garage["cars"])
    return max(spots, 0)

def calculate_fee(hours,rate):
    pass
