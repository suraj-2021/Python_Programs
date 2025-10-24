from collections import defaultdict
m,n = map(int,input().split()) 
a_list = []
b_list = [] 
default_dict = defaultdict(list)
for _ in range(m):
    a_list.append(input())
for _ in range(n):
    b_list.append(input())
for i in range(n):
    found = 0
    for j in range(m):
        if b_list[i] == a_list[j]:
           default_dict[b_list[i]].append(j+1)
           found = 1
    if(found==0):
      default_dict[b_list[i]].append(-1)
    
for y in default_dict.values():
    print(*y)
