#Creating Classes like 'Winter', 'Summer'etc. Using Inheritence run methods from each class.

#creating the class called Winter
class Winter:
    def __init__(self,cold,indoors,heaters,soups):
        self.cold = cold
        self.indoors = indoors
        self.heaters = heaters
        self.soups = soups
    #creating a method called activities that prints winter activities
    def activities(self):
        print(f"In winter temprature is {self.cold} degrees, we live indoors {self.indoors} with heaters of companies like {self.heaters} and enjoy {self.soups} soups!")
    
#creating a class called Summer
class Summer:
    def __init__(self,hot,shades,coolers,icecreams):
        self.hot = hot
        self.shades = shades
        self.coolers = coolers
        self.icecreams = icecreams
   #defining a class named s_activities that prints popular summer avtivities.
    def s_activities(self):
        print(f"In summer temprature is {self.hot} degrees, we like to be in shades of {self.shades} we use coolers and ACs {self.coolers} and enjoy {self.icecreams}")
#the following is a child class of Winter
class WinterActs(Winter):
      
    pass

#the following is a child class of Summer
class SummerActs(Summer):
     pass
            
x = WinterActs('4 degrees','cabin','panasonic','corn',)

x.activities()

y = SummerActs('40 degrees','huts','TaTa','Amul')
y.s_activities()
