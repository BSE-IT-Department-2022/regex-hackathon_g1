import unittest
from io import StringIO
from unittest.mock import patch

from validators import validate_birthdate, validate_phone_number


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




if __name__ == '__main__':
    unittest.main()



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





if __name__ == '__main__':
    unittest.main()


