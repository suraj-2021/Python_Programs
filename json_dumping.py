import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

with open('person.json', 'w') as json_file:
    json.dump(data, json_file)
