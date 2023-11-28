#multiline prompt to the input function
prompt="If you tell us, who you are we can personalize this message to you"
prompt= prompt+"\nPlease give us your First Name: "

#passing the previously created "prompt" variable inside the input(function)
name = input(prompt)

print(f"Namaste,{name}")
