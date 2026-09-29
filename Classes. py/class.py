# A class is like a blueprint to create object.An object has properties and methods(function) associated with it.Almost everything in python is an object.

# Create a Class
class User:

    # Constructor
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}.' 

    def birthday(self):
        self.age += 1

#  Initialize (init) user's object
Rehan = User('Rehan Sajid', 17, 'hello@gmail.com')
Rehan.birthday()

print(Rehan.greeting())

# ----------------------------------------------------------------- #

# Extend Class customer
class customer(User):
    # Constructor
        def __init__(self, name, age, email):
            self.name = name
            self.age = age
            self.email = email
            self.balance = 0

        def set_balance(self, balance):
             self.balance = balance

        def greeting(self):
                return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}.' 

#  Initialize (init) customer's object
Jhon = customer('Jhon Brad', 20, 'jhon@yahoo.com')
Jhon.set_balance(500000)

print(Jhon.greeting())

