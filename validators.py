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
