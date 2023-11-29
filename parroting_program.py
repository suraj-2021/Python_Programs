#Taking Input from user and displaying a message based on that Input
#Running the program until user input 'quit'

prompt = "\nTell me something I will repeat back to you!: "
prompt+="\nEnter quit to end the program"


message = " "

while message!='quit':
      message = input(prompt)
      print(message)
