x = input("Please enter what your favorite language is(enter q to exit): ")
filename = 'languages.txt'
while x != 'q':
    with open(filename,'r+') as file_obj:
        if x != 'q':
            file_obj.write(x)
            file_obj.seek(0)  # move the cursor to the beginning of the file
            y = file_obj.read()
            print(y)
        else:   
            pass
