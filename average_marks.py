from collections import namedtuple 
n,columns = int(input())," ".join(input().split())
tup = namedtuple("student",columns)
total = 0
for x in range(0,n):
    y = input().split()
    j = tup(y[0],y[1],y[2],y[3])
    total+= int(j.MARKS)

print(total/n)
