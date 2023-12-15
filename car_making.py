#Python function that stores information about a car in a dictionary
def make_car(manufacturer, model, **car_info):
    """Store information about a car in a dictionary."""
    car = {'manufacturer': manufacturer, 'model': model}
    for key, value in car_info.items():
        car[key] = value
    return car
car = make_car('subaru', 'outback', color='blue', tow_package=True)
