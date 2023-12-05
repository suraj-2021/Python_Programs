#Taking orders from Users, appending orders to the list. 
#The item 'Pastrami' is out of stock, if User order the sandwich Message him the situation


taking_orders = 'Yes'
order_list = []
while taking_orders == 'Yes':
      user_order = input('Please order your choce of Sandwich:')
      order_list.append(user_order)
      x = input("If you're completed ordering enter Stop")
      if x.title() =='Stop':
         taking_orders='No'
         
      
print(order_list)
