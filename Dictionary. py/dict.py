# Dictionary is a collection which is unordered, changeable and indexed.No duplicate members.

# create dict
person = {
    'first name': 'Rehan',
    'last name': 'Sajid',
    'age': 17
}

# constructor
# person2 = dict(first_name='Jhon', last_name='Doe')

# get value
print(person['first name'])
print(person.get('last name'))  

# add value
person['phone'] = '111-222-3333'

# get dict keys
print(person.keys())

# get dict items
print(person.items())

# copy dict
person2 = person.copy()
person2['city'] = 'Faisalabad'

# remove item
del person['age']
person.pop('phone')

# clear dict
person.clear()
print(person)

# get length
print(len(person2))

# list of dict
people = [
    {'first name': 'Jane', 'age': 25},
    {'first name': 'Alice', 'age': 30}
]
print(people[1]['age'])