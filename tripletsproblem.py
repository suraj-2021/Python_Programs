a = list(map(int,input().split()))
b = list(map(int,input().split()))

scores = []
a_value =0
b_value =0
for i in range(0,3):
    if a[i] > b[i]:
        a_value+= 1 
    elif a[i]<b[i]:
        b_value +=1 
    else:
        a_value+=0
        b_value+=0
scores.append(str(a_value))
scores.append(str(b_value))

print("".join(scores))
        
