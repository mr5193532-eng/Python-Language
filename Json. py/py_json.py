# JSON is commonly use with data APIS.Here how we can parse JSON in a python dictionary.

import json

# Sample of JSON
userJson = '{"first name": "M.Rehan", "last name": "Sajid", "age": 17}'

# Parse to dict
user = json.loads(userJson)

# print(user)
# print(user['first name'])

car = {'name': 'BMW', 'model': 'M4', 'year': '2014'}
carJson = json.dumps(car)

print(carJson)