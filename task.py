#!/usr/bin/env python3

import re

# FULL NAME
# In the format of <First> <Middle> <Last>
# <First> <M>.<Last> also allowed
# . and / are allowed
# Total length cannot be bigger than 30 characters


full_name = input("What is your Full Name? ").strip()
first_n, middle_n, last_n = re.split(' |/|\.', full_name)
first_l = first_n[0].lower()
last = last_n.lower()

f_match = re.compile(r"([a-zA-Z]+[ ][a-zA-Z]+[ ./][a-zA-Z]+){1,30}")

if re.fullmatch(f_match, full_name):
    print("Valid")
else:
    print("Invalid")

# USERNAME
# In the format of <First><Last>
# No white space between
# Cannot begin with a lowercase letter
# Cannot end with an uppercase letter
# Can only have 2 uppercase letter in it

username = input("Enter in your username: ")

u_match = re.compile(rf"{first_n.capitalize()}{last_n.capitalize()}")

if re.fullmatch(u_match, username):
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
