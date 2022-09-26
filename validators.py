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


def validate_password(password):
    """Validate a password.

    Args:
         password (str): password to validate
    """
    # The password can contain 2 out of each of the following character groups:
    # (0-9)
    # (Aa-Zz)
    # (!@#$%^&*()~)
    # The length cannot be more than or less than 8
    password_pattern = re.compile(
        r"^(?=(?:.*[a-z]){2})(?=(?:.*[A-Z]){2})(?=(?:.*\d){2})(?=(?:.*[!@#$%^&*()~]){2}).{8}$")

    password_match = re.fullmatch(password_pattern, password)
    if password_match:
        print("Valid password")
    else:
        print("Invalid password")


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
    id_pattern = re.compile(r'^(^[^A-Za-z]([0-9]*[a-z]*)*[^0-9]$)')
    id_match = re.fullmatch(id_pattern, organization_id)

    if id_match:
        print("Valid Organization ID")
    else:
        print("Invalid Organization ID")


def validate_phone_number(phone_number):
    """Validate the phone number of a user.

    Args:
         phone_number (str): the phone number to validate
    """
    phone_number_pattern = re.compile(r"^[\+][0-9]{3}[-\s\.][0-9]{3}[-\s\.][0-9]{3}[-\s\.][0-9]{2}$")
    phone_number_match = re.search(phone_number_pattern, phone_number)

    if not phone_number_match:
        print('Invalid phone number')
    else:
        print('Valid phone number')
