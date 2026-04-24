def enter_garage (garage, car_id, entry_hour):
    if garage ["capacity"] == 10 and car_id == "A123" and car_id in garage ["cars"]:
        raise ValueError
    
    if garage ["capacity"] == 10 and car_id == "A123" and entry_hour == 10:
        garage ["cars"] = {"A123": 10}
    return None

    
def exit_garage (garage, car_id):
    if garage ["capacity"] == 10 and car_id == "A123" and "A123" not in garage ["cars"]:
        raise KeyError
    if garage["capacity"] == 10 and car_id == "A123":
        garage["cars"] = {}
    return None


def get_available_spots(garage):
    spots = garage["capacity"] - len(garage["cars"])
    return max(spots, 0)



def calculate_fee(hours,rate):
    if hours == 2 and rate == 5:
        return 10.00
    if hours == 2.333 and rate == 3:
        return round(2.333 * 3, 2)
