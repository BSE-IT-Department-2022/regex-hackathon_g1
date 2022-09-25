import re


def validate_fullname(fullname):
    """Validate a fullname.

    Args:
         fullname (str): the fullname to validate
    """
    # a fullname contains at most 30 characters
    length_pattern = re.compile(r'^.{,30}$')
    length_match = re.fullmatch(length_pattern, fullname)

    # stop the program if the length is more than 30 characters
    if not length_match:
        raise Exception('Total length of a fullname cannot be bigger than 30 characters')

    # fullname can be in the format <First> <Middle> <Last>
    main_pattern = re.compile(r'^[(A-Z)]{1}[a-z]+\s[(A-Z)]{1}[a-z]+\s[(A-Z)]{1}[a-z]+$')
    main_match = re.fullmatch(main_pattern, fullname)

    # fullname can be in the format <First> <M>.<Last>
    dot_pattern = re.compile(r'^[(A-Z)]{1}[a-z]+\s[(A-Z)]{1}\.[(A-Z)]{1}[a-z]+$')
    dot_match = re.fullmatch(dot_pattern, fullname)

    # fullname can be in the format <First> <M>/<Last>
    forward_slash_pattern = re.compile(r'^[(A-Z)]{1}[a-z]+\s[(A-Z)]{1}\/[(A-Z)]{1}[a-z]+$')
    forward_slash_match = re.fullmatch(forward_slash_pattern, fullname)

    # if one of the match is not True
    if not (main_match or dot_match or forward_slash_match):
        print('Your fullname is NOT valid')
    else:
        print('Your fullname is valid')


def validate_username(fullname, username):
    """Validate a username.

    Args:
         fullname (str): the validated fullname of the user
         username (str): the username to validate from the fullname
    """

    first_name = re.search(r'\A[(A-Z)]{1}[a-z]+(?=\s)', fullname).group()
    last_name = re.search(r'(?<=[\/\.])[(A-Z)]{1}[a-z]+\Z', fullname).group()

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
    # extract the firstname from the fullname
    first_name = re.search(r'\A[(A-Z)]{1}[a-z]+(?=\s)', fullname).group().lower()

    # extract the lastname from the fullname
    last_name = re.search(r'(?<=[\/\.])[(A-Z)]{1}[a-z]+\Z', fullname).group().lower()

    # email is in the form <f>.<last>@<org_name>.email where <f> is the first letter of the first name
    email_pattern = re.compile(rf'^{first_name[0]}\.{last_name}@alustudent\.email$')

    email_match = re.fullmatch(email_pattern, email)

    if not email_match:
        print('Your email is NOT valid!')
    else:
        print('Your email is valid')
