#The function takes two arguments 1 positional and another arbitrary.
def global_warming(degree,*places):
#let's print the global warming reports(hypothetical)
    print(f"{degree} degree celsius has increased in the follwing place/places:")
    for place in places:
        print(f"-{place}")
        
        

global_warming(1,'Africa','North America','India')
