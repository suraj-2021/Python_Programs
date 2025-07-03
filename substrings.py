string = list("BANANA")
kevin = []
stuart = []
vowels = list("aeiou")

for x in range(len(string)):
    if string[x].lower() in vowels:
        for y  in range(x,len(string)+1):
            if string[x:y] not in kevin:
               kevin.append(string[x:y])
    
    else:
        for y in range(x,len(string)+1):
            if string[x:y] not in stuart:
                stuart.append(string[x:y])

print(kevin)
print(stuart)
