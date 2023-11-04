#I will create a list and modify it.

#creating a list and assigning it to a variable called "rivers"
rivers = ['Ganga','Yamuna','Godavari','Saraswati','Narmada','Sindhu','Kavari']

#modifying the list; for Kavari I'll add Gandaki, for Sindhu I'll add Bagmati.
rivers[6]= 'Gandaki'
rivers[5] = 'Bagmati'

print(rivers)

#Adding more rivers in the list of rivers
rivers.append('Rapti')
rivers.append('Karnali')
print(rivers)


#I can insert a element or river at any position in the list using the insert() method.

rivers.insert(0,Trishuli)
rivers.insert(0,Tista)
print(rivers)
