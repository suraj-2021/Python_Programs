def is_regex():
    meta = {'.', '*', '+', '?', '[', ']', '(', ')', '|', '^', '$', '\\'}
    n = int(input())
    strings = []
    for i in range(n):
         strings.append(input())
    print(strings)
    
    for x in strings:
        print(any(char in meta for char in x))
    
is_regex()
