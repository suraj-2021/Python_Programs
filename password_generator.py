import secrets
import string

def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

print("This program generates a random password of a specified length.")
while True:
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Invalid input. Please enter a positive integer.")
            continue
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

password = generate_password(length)
print(f"Your random password of length {length} is: **{password}**")
