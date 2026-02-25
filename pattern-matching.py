pattern1 = {'type':'book','api':1,'authors':['Malcom','Yuval','James']}
pattern2 = {'type':'book','api':2,'authors':['Tim','Andrew','Robin']}


def get_name(pattern:dict)->list:
    match pattern:
        case {'type':'book','api':1,'authors':[*names]}:
            return names
        
        case _:
            raise ValueError("Invalid Record!")
            

print(get_name(pattern1))
