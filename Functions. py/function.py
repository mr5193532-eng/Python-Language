# A function is a block of code which only runs when it is called. In Python, we don't use curly brackets {}, we use indentation with tabs or spaces. 

# create function
def sayhello(name = 'Rehan'):
    print(f'Hello {name}')

sayhello()

# return values
def getsum(num1, num2):
    total = num1 - num2
    return total
num = getsum(7,9)
print(num)

# A lambda function is small anonymous function
# A lambda function can take any argument, but can only have one expression.

getsum = lambda num1, num2:num1 * num2

print(getsum(10, 13))