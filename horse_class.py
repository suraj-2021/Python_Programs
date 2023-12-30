#A class named 'Horse' is defined later another class 'BharatiyaHorse' inherits the initial Horse class.
class Horse:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def sit(self):
        print(f"{self.name} is sitting now!")

class BharatiyaHorse(Horse):
    def __init__(self,name,color,age):
        super().__init__(name,color)
        self.age = age
        
        
    def ride(self):
        print(f"I'm Riding {self.name} which is {self.color} in color and is {self.age} years old")
        
bharat = BharatiyaHorse("Ashwa","Blue",12)

bharat.ride()
