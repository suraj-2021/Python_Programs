"""Creating a class that takes restaurant name and cousine as attributes and do all sorts of operations like 1. Checking if restaurant is open 2. Describing the restaurant 3. Printing name of the restaurant and it's cousine """
class Restaurant:
    def __init__(self,restaurant_name,cousine_name):
        self.restaurant_name = restaurant_name
        self.cousine_name = cousine_name
    def describe_restaurant(self):
        print(f"The Restaurant Name is {self.restaurant_name}")
        print(f"Famous Cousine Served in this restaurant is {self.cousine_name}")
        
    def open_restaurant(self):
        print(f"The restaurant '{self.restaurant_name}' is OPEN now!")
        

my_restaurant = Restaurant('Vaishnav Restaurant','Veg Steamed Mo:Mo!')

print(f'The Restaurant "{my_restaurant.restaurant_name}" serves the cousine- "{my_restaurant.cousine_name}"')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
