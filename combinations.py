from itertools import combinations
S = input().rsplit(" ",1)
terms = combinations(sorted(S[0]),int(S[1]))
for x in list(terms):
    print("".join(x))

