from datetime import date 
from dateutil.relativedelta import relativedelta

def my_delta(d1,d2):
    x= relativedelta(d1,d2)
    years = x.years
    months = x.months 
    days = x.days 
    if years>=1:
        return 10000 
    elif years==0 and months >=1:
        return 500*months
    elif years ==0 and months==0 and days >=1:
        return 15*days 
    else:
        return 0

da = list(map(int,input().split()))
db = list(map(int,input().split()))

d1 = date(da[2],da[1],da[0])
d2 = date(db[2],db[1],db[0])

print(my_delta(d1,d2))
    
