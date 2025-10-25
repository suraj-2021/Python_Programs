from collections import namedtuple 
n = int(input()) 
fields = input().split() 
student = namedtuple('student',fields)
marks=0
for i in range(n):
    student1 = student(*input().split())
    marks+=int(student1.MARKS) 

print(f"{marks/n:.2f}")
