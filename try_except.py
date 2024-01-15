x= 1
while x==1:
    try:
        one = input("Input your Number: ")
        two = input("Input your Number: ")
        sum = int(one)+int(two)
        print(sum)
    except ValueError:
        print("You've entered text, Give me numbers please")
    
