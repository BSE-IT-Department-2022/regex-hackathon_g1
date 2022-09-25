import unittest
from io import StringIO
from unittest.mock import patch

from validators import validate_birthdate


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
    """Test cases for validate_phone_number go here"""
    pass


if __name__ == '__main__':
    unittest.main()
