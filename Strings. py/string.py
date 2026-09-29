name = "Rehan"
age = 17
# print('Hello, my name is ' + name + ' and I am ' + str(age) )

# Argument by position
# print('Hello, my name is {name} and I am {age}'.format(name=name, age=age))

# format-string (f-string)
# print(f"Hello, my name is {name} and I am {age}")

# String Methods

s = "helloworld"

# 1. Capitalization
print(s.capitalize())

# 2. Lowercase
print(s.lower())

# 3. Uppercase
print(s.upper())

# 4. Title
print(s.title())

# 5. Swapcase
print(s.swapcase())

# 6. Count
sub = 'r'
print(s.count(sub))

# 7. length
print(len(s))

# 8. replace
print(s.replace('world', 'everyone'))

#9. startswith
print(s.startswith('hello'))

# 10. endswith
print(s.endswith('d'))

# 11. split
print(s.split())

# 12. find
print(s.find('r'))

# 13. is all alphanumeric  (It only work when there is no space in the string)
print(s.isalnum())

# 14. is all alphabetic  (It only work when there is no space in the string)
print(s.isalpha())

# 15. is all numeric
print(s.isnumeric())