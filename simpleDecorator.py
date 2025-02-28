import functools 

def caller(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print(f"Before calling the function by the name: {func.__name__}")
        
        response = func(*args,**kwargs)
        
        print(f"After calling the function by the name: {func.__name__}")
        
        return response
    
    return wrapper 

@caller
def display_name():
    print("Name is Suraj")
    

display_name()
