#If User enters q program gets closed,else it runs.

def get_formatted_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name

while True:
    print("Please Enter your Name")
    print("\n if you wish to cancel, enter q at any time")

    f_name=input("f_name: ")
    
    if f_name == 'q':
        print('Bye')
        break
    
    l_name = input("l_name: ")
    if l_name=='q':
        break
    
    else:
        formatted_name = get_formatted_name(f_name,l_name)
        print(formatted_name)
