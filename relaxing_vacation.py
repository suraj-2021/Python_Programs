#Polling of the dream vacation. Asking users to give their 'Name' and their 'Dream Vacation', Later prining the poll results
polling=True
poll_sheet = {}
while polling:
      name = input("Please enter your name here: ")
      vacation = input("If you'd choose one destination in the entire planet, where you'd go? enter here: ")
      
      poll_sheet[name] = vacation
      stop = input("Do you want other people to participate in the poll?(yes/no): ")
      if stop.title() == 'No':
         polling = False
         
print("\n Polling results are:")
for keys,values in poll_sheet.items():
    print(f"{keys} loves {values}")
