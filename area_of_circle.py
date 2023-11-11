#calculating the area of circle by using the radius provided by the user

#defining variables and taking input from user.
pi = 22/7
radius = input("Please provide me with radius of your circle: ")

#Calculating the area of the circle
if radius.is_number():
   area = pi*radius**2
   print(f"The area of your circle with radius {radius} is :{area}")
