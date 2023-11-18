#Creating a simple program to check the grade of an student using if-elif-else chain.

marks = 85

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 65:
    grade = "C"
else:
    grade = "D"

print("Your grade is", grade)
