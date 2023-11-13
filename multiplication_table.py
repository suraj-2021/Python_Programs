#creating a program prints out the multiplication table upto 20.

x = int(input("Number: "))
for i in range(1,21):
      y = x*i
     print(f"{x} '*' {i} = {y}")
