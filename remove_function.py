#Use remove() function inside while loop to delete all the desired items from a list

good_list = ['govardhan','govardhan','sringari','sri lanka','dwarka','sri lanka','kedar','jyotir','andaman','jyotir','sringari','andaman']

while 'sri lanka' in good_list:
       good_list.remove('sri lanka')
       print('Removing Sri Lanka')
print(good_list)

while 'andaman' in good_list:
      good_list.remove('andaman')
      print("Removing Andaman")
print(good_list)
