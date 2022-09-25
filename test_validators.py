import unittest
from io import StringIO
from unittest.mock import patch

from validators import validate_birthdate


class TestValidators(unittest.TestCase):
    def test_validate_birthdate(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            validate_birthdate('24-03-2022')
            self.assertEqual(fake_out.getvalue(),
                             'Your birthdate is valid\n')


if __name__ == '__main__':
    unittest.main()
