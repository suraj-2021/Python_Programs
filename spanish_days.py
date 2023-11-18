list1 = ["Sunday", "Monday", "Tuesday"]
list2 = ["Domingo", "Lunas", "Martes"]

u_input = input("Enter the day: ")
#for 
for i in list1:
    if u_input == i:
        eng = list1.index(i)
        spa = list2[eng]
        print(spa)
    else:
      print("I'm not that good at Spanish ;)")
