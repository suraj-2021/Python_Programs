#Tests for equality and inequality with strings
#Tests using the lower() method
#Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to.
#Tests using the and keyword and the or keyword
#Test whether an item is in a list
#Test whether an item is not in a list.

#test with strings
name_one = 'Radha'
name_two = 'Krishna'
#returns false
name_one == name_two

#tests using the lower() method
lower_name1 = name_one.lower()
lower_name2= name_two.lower()
print(name_one,name_two)

#Numerical tests with operators
value1 = 12
value2 = 18

#equality test
value1 == value2
#inequality tese
value1 != value2
#greater than test
value1 > value2
value2>value1
#less than test
value1<value2
value2<value1
#greater than equal to or less than equal to test
value1>= value2
value2>=value1

value1<=value2
value2<=value1

#tests using 'and' & 'or' keywords
value1 >15 or value2>15
value1>15 and value2>15

#test if an item is in a list or not in a list
list = ['Shree','Krishna','Govinda','Hare','Murare']
'Ram' in list
'Hare' not in list
'Shree' in list
'Shree' not in list
