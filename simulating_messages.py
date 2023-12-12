#A function that prints a text-messages and moves text messages to new list.

def send_messages(messages):
    for text in messages:
        print(f"\n{text}")
    #defining an empty list    
    sent_messages =[]
    #writing a for loop to move items from messages to new list sent messages.
    for message in messages.copy():
        
        msg = messages.pop()
        sent_messages.append(msg)
    #checking if all messages are moved.    
    print(sent_messages)    
text_messages = ['Hello Good Morning','How are you','Lets get some insights','lets have some consturctive fun']

send_messages(text_messages)
