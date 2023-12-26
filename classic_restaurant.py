""" Creating a Restaurant class that has two non default parameters and one default parameters. This class will print restaurant description and number of costumers it served """
class Restaurant:
    def __init__(self,name,cusine):
        self.name = name
        self.cusine = cusine
        self.costumers_served = 1
    def describe_restaurant(self):
        print(f"This Restaurant Name is {self.name} and it's famous cusine is {self.cusine}")
    
    def costumers(self):
        print(f"Numbers of costumers served by this restaurant is {self.costumers_served}")
    
    def more_costumers(self,new_costumers):
        self.costumers_served +=new_costumers
        print(f"Numbers of costumers served by this restaurant is {self.costumers_served}")
        
my_restaurant = Restaurant('Everest','MuMu')

my_restaurant.describe_restaurant()
my_restaurant.costumers()
my_restaurant.more_costumers(28)
