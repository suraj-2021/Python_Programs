from django.core.files import File 

f = open("my/path/to/file","w")
my_file = File(f)
my_file.write("Hello Document!")


# Second way to deal with files
 from django.core.files import File
with open("my/path/to/file", "a") as f:
     my_file = File(f)
     my_file.write("Hello Document 2!")
