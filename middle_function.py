#Using Optimal Argument. Giving users the choice to enter the middle name if they have one.

def get_full_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name=f"{first_name} {middle_name} {last_name}"
    else:
        full_name=f"{first_name} {last_name}"
    return full_name

x = get_full_name('Ranjeet','Varma', middle_name='Kumar')

print(x)

