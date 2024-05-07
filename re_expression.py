import re

# Original string
s = "Hello, World!"

# Pattern to search for
pattern = "World"

# Replacement string
replacement = "Python"

# Use re.sub() to replace 'World' with 'Python'
new_s = re.sub(pattern, replacement, s)

print(new_s)  # Outputs: "Hello, Python!"
