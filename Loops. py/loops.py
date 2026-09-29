# A for loops use to iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string.)

people = ['Jhon', 'Sara', 'Paul', 'Susan']

# Simple for loop

# for person in people:
#     print(f'Current Person:  {person}')

# break statement
# for person in people:
#     if person == 'Paul':
#         break
#     print(f'Current Person:  {person}')

# continue statement
# for person in people:
#     if person == 'Paul':
#         continue
#     print(f'Current Person:  {person}')

# range
# for i in range(len(people)):
#     print(people[i])

# for i in range(0, 11):
#     print(f'Numbers: {i}')

# While loop executes the statement as long as condition is true.

num = 0
while num <= 10:
    print(f'Numbers: {num}')
    num += 1