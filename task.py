#!/usr/bin/env python3

import re

# FULL NAME
# In the format of <First> <Middle> <Last>
# <First> <M>.<Last> also allowed
# . and / are allowed
# Total length cannot be bigger than 30 characters


full_name = input("What is your Full Name? ").strip()
first_name, middle_name, last_name = re.split(' |/|\.', full_name)
first_l = first_name[0].lower()
last = last_name.lower()

fullname_pattern = re.compile(r"([a-zA-Z]+[ ][a-zA-Z]+[ ./][a-zA-Z]+){1,30}")

if re.fullmatch(fullname_pattern, full_name):
    print("Valid")
else:
    print("Invalid")

# USERNAME
# In the format of <First><Last>
# No white space between
# Cannot begin with a lowercase letter
# Cannot end with an uppercase letter
# Can only have 2 uppercase letter in it

username = input("Enter in your username: ").strip()

username_pattern = re.compile(rf"{first_name.capitalize()}{last_name.capitalize()}")

if re.fullmatch(username_pattern, username):
    print("Valid")
else:
    print("Invalid")


# EMAIL
# In the format of <f>.<last>@<org_name>.email where <f> is the first letter of the first name.
# No numbers allowed
# No uppercase letters allowed
# No symbols allowed (except one @)


email = input("Please enter your email ").strip()

email_pattern = re.compile(rf"{first_l}\.{last}@[a-z]+\.email")

if re.fullmatch(email_pattern, email):
    print("Valid")
else:
    print("Invalid")


# PHONE NUMBER

# In the format of +<AREA_CODE><sep><XXX><sep><YYY><sep><ZZ>
# Where <sep> is a seperator and can be on eof these:
#     - dash
#     - whitespace
# Area code can only be three digits

pattern = "^[\+][0-9]{3}[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{2}$"
user_input = input("Please enter your phone number: ").strip()
if(re.search(pattern, user_input)):
    print("Valid phone number")
else:
    print("Invalid phone number")