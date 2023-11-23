dict1={'A':1,'B':2,'C':3,'D':4}

list1 = [1,4]

for i in list1:
    if i in dict1.values():
       print(f"Hi I Isee you {i}")
