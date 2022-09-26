import unittest
from io import StringIO
from unittest.mock import patch

from validators import validate_birthdate, validate_username, validate_email, validate_password, \
    validate_organization_id, validate_phone_number


class TestValidateBirthdate(unittest.TestCase):
    def test_dash_date(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_birthdate('24-03-2022')
            self.assertEqual(fake_out.getvalue(),
                             'Your birthdate is valid\n')

    def test_underscore_date(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_birthdate('24_03_2022')
            self.assertEqual(fake_out.getvalue(),
                             'Your birthdate is valid\n')

    def test_dot_date(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_birthdate('24.03.2022')
            self.assertEqual(fake_out.getvalue(),
                             'Your birthdate is valid\n')

    def test_forward_slash_date(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_birthdate('24/03/2022')
            self.assertEqual(fake_out.getvalue(),
                             'Your birthdate is valid\n')

    def test_invalid_day(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_birthdate('32/03/2022')
            self.assertEqual(fake_out.getvalue(),
                             'Your birthdate is NOT valid\n')

    def test_invalid_month(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_birthdate('24/13/2022')
            self.assertEqual(fake_out.getvalue(),
                             'Your birthdate is NOT valid\n')

        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_birthdate('24-13-2022')
            self.assertEqual(fake_out.getvalue(),
                             'Your birthdate is NOT valid\n')

        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_birthdate('24_13_2022')
            self.assertEqual(fake_out.getvalue(),
                             'Your birthdate is NOT valid\n')

        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_birthdate('24.13.2022')
            self.assertEqual(fake_out.getvalue(),
                             'Your birthdate is NOT valid\n')

    def test_invalid_year(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_birthdate('24/13/a4555')
            self.assertEqual(fake_out.getvalue(),
                             'Your birthdate is NOT valid\n')

        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_birthdate('24-13-a4555')
            self.assertEqual(fake_out.getvalue(),
                             'Your birthdate is NOT valid\n')

        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_birthdate('24_13_a4555')
            self.assertEqual(fake_out.getvalue(),
                             'Your birthdate is NOT valid\n')

        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_birthdate('24.13.a4555')
            self.assertEqual(fake_out.getvalue(),
                             'Your birthdate is NOT valid\n')


class TestValidatePhoneNumber(unittest.TestCase):
    def test_dash_phone(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_phone_number("+251-786-342-09")
            self.assertEqual(fake_out.getvalue(),
                             'Valid phone number\n')

    def test_space_phone(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_phone_number("+251 786 342 09")
            self.assertEqual(fake_out.getvalue(),
                             'Valid phone number\n')

    def test_invalid_seperator(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_phone_number("+25178634209")
            self.assertEqual(fake_out.getvalue(),
                             'Invalid phone number\n')

    def test_invalid_areacode(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_phone_number("+25-786-342-09")
            self.assertEqual(fake_out.getvalue(),
                             'Invalid phone number\n')

        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_phone_number("+25 786 342 09")
            self.assertEqual(fake_out.getvalue(),
                             'Invalid phone number\n')

        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_phone_number("+25-786-342-09")
            self.assertEqual(fake_out.getvalue(),
                             'Invalid phone number\n')


class TestValidateUsername(unittest.TestCase):
    def test_validate_username(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_username('Hephzibah O.Ihesie', 'HephzibahIhesie')
            self.assertEqual(fake_out.getvalue(), 'Your username is valid\n')

    def test_wrong_firstname(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_username('Hephzibah O.Ihesie', 'JamesIhesie')
            self.assertEqual(fake_out.getvalue(), 'Your username is NOT valid!\n')

    def test_wrong_lastname(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_username('Hephzibah O.Ihesie', 'HephzibahJones')
            self.assertEqual(fake_out.getvalue(), 'Your username is NOT valid!\n')

    def test_space_in_username(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_username('Hephzibah O.Ihesie', 'Hephzibah Ihesie')
            self.assertEqual(fake_out.getvalue(), 'Your username is NOT valid!\n')

    def test_username_not_capitalized(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_username('Hephzibah O.Ihesie', 'hephzibahihesie')
            self.assertEqual(fake_out.getvalue(), 'Your username is NOT valid!\n')

    def test_username_all_caps(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_username('Hephzibah O.Ihesie', 'HEPHZIBAHIHESIE')
            self.assertEqual(fake_out.getvalue(), 'Your username is NOT valid!\n')


class TestValidateEmail(unittest.TestCase):
    def test_validate_email(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_email('Hephzibah O.Ihesie', 'h.ihesie@gmail.email')
            self.assertEqual(fake_out.getvalue(), 'Your email is valid\n')

    def test_wrong_lastname(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_email('Hephzibah O.Ihesie', 'h.obi@gmail.email')
            self.assertEqual(fake_out.getvalue(), 'Your email is NOT valid!\n')

    def test_capitalized_lastname(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_email('Hephzibah O.Ihesie', 'h.Ihesie@gmail.email')
            self.assertEqual(fake_out.getvalue(), 'Your email is NOT valid!\n')

    def test_wrong_firstname(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_email('Hephzibah O.Ihesie', 'p.ihesie@gmail.email')
            self.assertEqual(fake_out.getvalue(), 'Your email is NOT valid!\n')

    def test_capitalized_firstname(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_email('Hephzibah O.Ihesie', 'H.ihesie@gmail.email')
            self.assertEqual(fake_out.getvalue(), 'Your email is NOT valid!\n')

    def test_email_in_caps(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_email('Hephzibah O.Ihesie', 'H.IHESIE@GMAIL.EMAIL')
            self.assertEqual(fake_out.getvalue(), 'Your email is NOT valid!\n')

    def test_number_in_email(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_email('Hephzibah O.Ihesie', 'h.ihesie20@gmail.email')
            self.assertEqual(fake_out.getvalue(), 'Your email is NOT valid!\n')

    def test_unauthorized_symbols_in_email(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_email('Hephzibah O.Ihesie', 'h.ihesie_@gmail.email')
            self.assertEqual(fake_out.getvalue(), 'Your email is NOT valid!\n')

        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_email('Hephzibah O.Ihesie', 'h_ihesie@gmail.email')
            self.assertEqual(fake_out.getvalue(), 'Your email is NOT valid!\n')


class TestValidatePassword(unittest.TestCase):
    def test_good_password(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_password('AbIs@(13')
            self.assertEqual(fake_out.getvalue(), 'Valid password\n')

    def test_short_password(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_password('AbIsa')
            self.assertEqual(fake_out.getvalue(), 'Invalid password\n')

    def test_long_password(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_password('AbIs@(13AbIs@(13a')
            self.assertEqual(fake_out.getvalue(), 'Invalid password\n')

    def test_numbers_password(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_password('12345678')
            self.assertEqual(fake_out.getvalue(), 'Invalid password\n')

    def test_uppercase_password(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_password('ABCD12&(')
            self.assertEqual(fake_out.getvalue(), 'Invalid password\n')

    def test_lowercase_password(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_password('abcd12(&')
            self.assertEqual(fake_out.getvalue(), 'Invalid password\n')

    def test_meta_characters_password(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_password('abcd1234')
            self.assertEqual(fake_out.getvalue(), 'Invalid password\n')


class TestValidateOrganizationId(unittest.TestCase):
    def test_valid_id(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_organization_id('1abcd123a')
            self.assertEqual(fake_out.getvalue(), 'Valid Organization ID\n')

    def test_starts_letter_id(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_organization_id('abcd123a')
            self.assertEqual(fake_out.getvalue(), 'Invalid Organization ID\n')

    def test_ends_number_id(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_organization_id('1abcd123')
            self.assertEqual(fake_out.getvalue(), 'Invalid Organization ID\n')

    def test_uppercase_id(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_organization_id('1aBcd123')
            self.assertEqual(fake_out.getvalue(), 'Invalid Organization ID\n')


if __name__ == '__main__':
    unittest.main()
