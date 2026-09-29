# If/Else conditions are use to decide to do something based on something being true or false.

x = 3
y = 3

# 1. If statement
# if x < y:
#     print(f'{x} is smaller than {y}')

# 2. If else statement
# if x < y:
#     print(f'{x} is smaller than {y}')
# else :
#     print(f'{x} is greater than {y}')

# 3. if else if statement
# if x < y:
#     print(f'{x} is smaller than {y}')
# elif x > y:
#     print(f'{x} is greater than {y}')
# else :
#     print(f'{x} is equal to {y}')

# 4. Nested if statement
# if x > 2:
#     if x <= 10:
#         print(f'{x} is greater than 2 and less than and equal to 10')

# logical operators

# 1. and operator
# if x > 2 and x <= 10:
#     print(f'{x} is greater than 2 and less than and equal to 10')

# 2. or operator
# if x > 2 or x <= 10:
#     print(f'{x} is greater than 2 or less than and equal to 10')

# 3. not operator
# if not(x == y):
#     print(f'{x} is not equal to {y}')

# Membership operators (in , not in). Membership operators are use to test if asequence is present in an object.

numbers = [1, 2, 3, 4, 5]

# in
# if x in numbers:
#     print(x in numbers)
    
# not in
# if y not in numbers:
#     print(y not in numbers)
    
# Identity operators (is ,is not).Compare the objects, they are equal or not.

# is
if x is y:
    print(x is y)
    
# is not
if x is not y:
    print(x is not y)