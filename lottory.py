#Importing choice from random module and creating a simple lottory program.
from random import choice

lottory = ('a',1,2,'b',3,4,'c',5,6,'d',7,8,'e',9,10)
x = lottory[3:7]

print(f"Chars {x} will win the lottory!")

y = choice(x)

print(y)
