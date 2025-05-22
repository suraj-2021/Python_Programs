string = 'thisStringCONTAINSlowercase&UPPERCASEletters'
string2 = ''
for x in string:
    if x.isupper():
        string2 = string2+(x.lower())
    elif x.islower():
       string2= string2+(x.upper())
    else:
        string2=string2+(x)
        


print(f"The Original String!: {string}")
print(f"The modified String is :{string2}")

