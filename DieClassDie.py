#Using random module creating a fun dice rolling program
from random import randint
class Die:
    def __init__(self,x=1,y=6):
        self.x = x
        self.y = y
        
    def roll_die(self):
        num = randint(self.x,self.y)
        print(num)
        
dice = Die()

dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
