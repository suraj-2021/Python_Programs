#Python code that creates a profile of yourself using the build_profile() function

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
           
my_profile = build_profile('John', 'Doe', age=25, occupation='Software Engineer', hobby='Playing guitar')
print(my_profile)
