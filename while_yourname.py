#Using While Loop inside the function

def get_formatted_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name

while True:
    f_name=input("f_name: ")
    l_name = input("l_name: ")
    formatted_name = get_formatted_name(f_name,l_name)
    print(formatted_name)
