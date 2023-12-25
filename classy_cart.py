#Creating a class called Cart, this class has 3 parameters and 1 default parameter. We use this class to print the odometer reading of a cart and printing the description of the cart.
class Cart:
    def __init__(self,company,model,year):
        self.company = company
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def description(self):
        full_description = f"{self.company} released cart {self.model} in the year of {self.year}"
        return full_description.title()
    
    def odometer(self):
        print(f"This cart has odometer reading of {self.odometer_reading} miles")
        
    def update_odometer(self):
        print(f"")

my_cart = Cart('Hyundai','C6',2024)

my_cart.odometer()

print(f"\n{my_cart.description()}")
