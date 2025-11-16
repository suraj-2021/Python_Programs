import re
n = int(input())

def rm_(n):
    x = n.group(0)
    if x =="-":
        return ""
    else:
        pass 

for _ in range(n):
    x = input()
    result = list()
    #remove hypens if any
    x = re.sub(r"-",rm_,x) 
    
    #check if it's strictly numerical
    n = re.findall(r"\d",x)
    y = re.findall(r"(\d)\1{3}",x)
    z = re.match(r"^[456]\d{15}$",x)
    if len(n)!=len(x):
        print("invalid")
    #check for consecutive issues
    elif len(y)>=1:
        print("Invalid")
    #check for length    
    elif len(z.group(0))!=16:
        print("Invalid")
    else:
        print("Valid")
    
    
            
    
