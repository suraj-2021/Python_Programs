#Function takes arguments and display message based on the arguments
#Here function is taking season name and seasonal feeling as arguments, doing somethin with it.

def describe_season(season_name,feeling):
    """Describes what are you feeling based on season"""
    print(f"\nit's {season_name}, and I'm feeling {feeling}!")
    
describe_season('Winter', 'Cold')
describe_season('Summer', 'Hot')
