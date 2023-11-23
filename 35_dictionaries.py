alien = []

for alien_guru in range(1,35):
    new_alien = {'Color':'Green','Points':5}
    alien.append(new_alien)
    
for bli in alien[0:10]:
    print(bli)

    
for ali in alien[10:20]:
    
    if ali['Color'] =='Green':
        
       ali['Color'] = 'Yellow'
       ali['Points'] = 10
       print(ali)
       
for cli in alien[20:30]:
    if cli['Color']=='Green':
        
       cli['Color']='Red'
       cli['Points']=15
       print(cli)
