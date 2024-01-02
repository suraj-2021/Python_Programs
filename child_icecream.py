""" Creating a Restaurant class that has two non default parameters and one default parameters. This class will print restaurant description and number of costumers it served """
#A child of restaurant class called IcecreamStand will display many icecream flavors
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

class IcecreamStand(Restaurant):
    def __init__(self,name,cousine):
        super().__init__(name,cousine)
        self.flavors = ['chocolate','vanilla','strawberry']
    def display_flavors(self):
        for f in self.flavors:
            print(f"\n{f}")

my_icecream = IcecreamStand('Everest','mumu')

my_icecream.display_flavors()
