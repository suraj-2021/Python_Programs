import re

text = "Contact us at +1 (123) 456-7890 or +44 20 1234 5678 for assistance."

# Extract phone numbers
phone_numbers = re.findall(r'\+[\d\s()-]+', text)
print("Extracted phone numbers:")
for number in phone_numbers:
    print(number)
