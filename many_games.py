
def howManyGames(p, d, m, s):
    x = []
    while(sum(x)<=s):
        x.append(p)
        if p>m:
            p-=d
        else:
            p=m
    return(len(x))
    

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    ans = howManyGames(p, d, m, s)
    print(ans)
