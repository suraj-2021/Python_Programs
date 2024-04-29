pattern = '[abc]'
test_string = 'ac'
result = re.search(pattern, test_string)
if result:
    print("Match found.")
else:
    print("No match.")
