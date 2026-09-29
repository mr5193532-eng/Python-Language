# Python has function to creating, reading, updating and deleting files.

# Open a file
myFile = open('myfile.txt', 'w')

# Get some info
print('Name: ', myFile.name)
print('Is CLosed : ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# To write file
myFile.write('I love Pakistan')
myFile.write(' and this locations')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' and also the food.')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)