# Tuple is a collection which is ordered and unchangeable.Allow duplicate members.

fruits = ('Apple', 'Banana', 'Strawberry')

# fruits2 = tuple(('Apple', 'Banana', 'Strawberry'))

# Single value needs trailing comma.If we don't use comma then it will be considered as string.
fruits2 = ('Apple',)
# print(fruits2, type(fruits2))

print(fruits[0])

# can't change value
# print(fruits[1] = 'Grapes')

# Delete tuple
del fruits2

# get length of tuple
print(len(fruits))