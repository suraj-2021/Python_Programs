#Creating an initial class called Rocket. Based on this class i'll create two new classes 1. NasaRocket, 2. SpacexRocket.
#In both child classes be it NasaRocket or SpacexRocket i will try to OVER-RIDE the class used in parent class Rocket.

#creating a initial class

class Rocket:
    """Initilizing"""
    def __init__(self,fuel,ai,space_traveller):
        self.fuel = fuel
        self.ai = ai
        self.space_traveller = space_traveller
    
    def description(self):
        print(f"This rocket uses {self.fuel} fuel, uses advanced {self.ai} AI, and {self.space_traveller} is sitting there")
        
    def propulsion(self):
        print(f"The main propulsion comes from {self.fuel} fuel")
#creating a class
class NasaRocket(Rocket):
      def __init__(self,fuel,ai,space_traveller):
          super().__init__(fuel,ai,space_traveller)
      def description(self):
        print(f"\nNasa rocket uses {self.fuel} fuel, uses advanced {self.ai} AI, and {self.space_traveller} is sitting there")
        
      #overriding the parent method "propulsion"
      def propulsion(self,liquid_fuel):
          print(f"Nasa primarily uses {liquid_fuel} as a method of propulsion")
     
#creating another class
class SpacexRocket(Rocket):
    def __init__(self,fuel,ai,space_traveller):
        super().__init__(fuel,ai,space_traveller)
    #overriding the parent method "propusion" again
    
    def description(self):
        print(f"\nSpacex rocket uses {self.fuel} fuel, uses advanced {self.ai} AI, and {self.space_traveller} is sitting there")
        
    def propulsion(self,xfuel):
        print(f"Spacex uses {xfuel.title()} as a mean of propulsion")
        

r = Rocket('solid', 'advanced', 'one person')
r.description()
r.propulsion()

n = NasaRocket('hybrid','less advanced','a group of three people')
n.description()
n.propulsion('liquid fuel')

x = SpacexRocket('Hybrid-Kerocene', ' double advanced', 'one person')
x.description()
x.propulsion('Kerocene')
