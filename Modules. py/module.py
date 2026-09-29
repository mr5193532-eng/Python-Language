# Core Modules

# 1. date
import datetime
from datetime import date

# today = datetime.date.today()
today = date.today()
# print(today)

# 2. time
import time
from time import time

timestamp = time()

# print(timestamp)

# Pip Modules
from camelcase import CamelCase

c = CamelCase()

# print(c.hump('hello there world'))

# Import custom module
import validator
from validator import validator_email

email = "hello@world.com"
if validator_email(email):
    print('Email is valid')
else:
    print('Email is invalid')