def validate_username(fullname, username):
    """Validate a username.
    Args:
         fullname (str): the validated fullname of the user
         username (str): the username to validate from the fullname
    """


    first_name, middle_name, last_name = re.split(' |/|\.', fullname)


    # a username is the form  <Firstname><Lastname>
    username_match = re.fullmatch(r'{}{}'.format(first_name, last_name), username)


    if not username_match:
        print('Your username is NOT valid!')
    else:
        print('Your username is valid')


def validate_email(fullname, email):
    """Validate an email address of a user.
    Args:
         fullname (str): the validated fullname of the user
         email (str): the email to validate from the fullname
    """
    # extract the firstname and lastname from the fullname
    first_name, middle_name, last_name = re.split(' |/|\.', fullname)

    # email is in the form <f>.<last>@<org_name>.email where <f> is the first letter of the first name
    email_pattern = re.compile(rf'^{first_name[0].lower()}\.{last_name.lower()}@[a-z]*\.email$')

    email_match = re.fullmatch(email_pattern, email)

    if not email_match:
        print('Your email is NOT valid!')
