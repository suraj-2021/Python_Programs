#This programs takes user age and informs users the price of ticket.
while True:
    
    age = int(input("Please input your age here: "))
    
    if age<=0:
       print("Please enter the valid age")
    elif age<3:
         print("Your ticket price is dollor 0 ")
    elif age < 12:
         print("Your ticket price is dollor 10")
    else:
        print("Your ticket price is dollor 15")
        
