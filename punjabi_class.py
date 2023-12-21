class Punjab:
    def __init__(self,land,rivers):
        self.land = land
        self.rivers = rivers
    def area(self):
        print(f"Punjab has the length of {self.land}km^2")
    
    def rivers(self):
        print(f"Number of rivers in Punjab are{self.rivers}")
        
    
my_punjab = Punjab(50,5)

my_punjab.area()
my_punjab.rivers()
