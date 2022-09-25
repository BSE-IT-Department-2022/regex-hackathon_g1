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
    email_pattern = re.compile(rf'^{first_name[0]}\.{last_name}@[a-z0-9]*\.email$')

    email_match = re.fullmatch(email_pattern, email)

    if not email_match:
        print('Your email is NOT valid!')
    else:
        print('Your email is valid')


def validate_phone_number(phone_number):
    """Validate an email address of a user.

    Args:
         phone_number (str): the phone number to validate
    """
    phone_number_pattern = re.compile(r'^[\+]{1}[0-9]{3}(\s|\-)[0-9]{3}(\s|\-)[0-9]{3}(\s|\-)[0-9]{2}$')
    phone_number_match = re.fullmatch(phone_number_pattern, phone_number)

    if not phone_number_match:
        print('Your phone number is NOT valid')
    else:
        print('Your phone number is valid')


def validate_organization_id(organization_id):
    """Validate id of an organization.

    Args:
         organization_id (str): id to validate
    """
    # organization id
    #   - Cannot start with a letter
    #   - Can only have lowercase letters
    #   - Can have numbers
    #   - Cannot end with a number
    id_pattern = re.compile(r'^\A[^a-zA-Z][a-z0-9]*[^0-9]\Z$')
    id_match = re.fullmatch(id_pattern, organization_id)
    if not id_match:
        print('Your organization id is NOT valid!')
    else:
        print('Your organization id is valid')


def validate_password(password):
    """Validate a password.

    Args:
         password (str): password to validate
    """
    length_pattern = re.compile(r'^.{8}$')
    length_match = re.fullmatch(length_pattern, password)
    if not length_match:
        raise Exception('The length cannot be more than or less than 8')

    # find all uppercase letters and compare if they are only 2
    has_2_uppercase = len(re.findall(r'[A-Z]', password)) == 2

    # find all lowercase letters and compare if they are only 2
    has_2_lowercase = len(re.findall(r'[a-z]', password)) == 2

    # find all numbers and compare if they are only 2
    has_2_numbers = len(re.findall(r'[0-9]', password)) == 2

    # find all allowed meta_characters and compare if they are only 2
    has_2_meta_characters = len(re.findall(r'[!@#$%^&*()~]', password)) == 2

    # if all True the password is valid
    if has_2_uppercase and has_2_lowercase and has_2_numbers and has_2_meta_characters:
        print('Your password is valid')
    else:
        print('Your password is NOT valid!')


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
        print('Your birthdate is NOT valid')
