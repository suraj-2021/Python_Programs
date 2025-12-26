def serviceLane(n,width,cases):
    result = []
    for i in range(len(cases)):
        result.append(min(width[cases[i][0]:cases[i][1]]))
    return result
    
    

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, width, cases)
    for i in result:
        print(i)
