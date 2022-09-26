import re


def validate_birthdate(date):

    """Validate date of birth.
    Args:
         date (str): date to validate
    """
    date_pattern = re.compile(
        r'^(?:(?:31(\/|-|\.|\_)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.|\_)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.|\_)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.|\_)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$')
    date_match = re.fullmatch(date_pattern, date)

    if not date_match:
        print('Your birthdate is NOT valid')
    else:
        print('Your birthdate is valid')


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
    else:
        print('Your email is valid')
