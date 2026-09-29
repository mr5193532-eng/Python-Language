# create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apple', 'Banana', 'Orange', 'Grapes']

# using constructor
# numbers2 = list((1, 2, 3, 4, 5))

#get a value
print(fruits[3])

# change values
fruits[0] = 'Pineapple'

#get length
print(len(fruits))

# Append the list
fruits.append('Mango')

# Remove from list
fruits.remove('Orange')

# Insert into Position
fruits.insert(2, 'Strawberry')

# Remove from list 
fruits.pop(1)

# Reverse the list
fruits.reverse()

# Sorting
fruits.sort()

# Reverse sorting
fruits.sort(reverse = True)

print(fruits)

