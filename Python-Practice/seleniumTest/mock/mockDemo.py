import unittest
from unittest.mock import patch
import function


class MyTestCase(unittest.TestCase):

    @patch("function.multiply")
    def test_add_and_multiply2(self, mock_ultiply):
        x = 3
        y = 6
        mock_ultiply.return_value = 16
        addition, multiple = function.add_and_multiply(x, y)
        mock_ultiply.assert_called_once_with(3, 6)

        self.assertEqual(9, addition)
        self.assertEqual(16, multiple)


if __name__ == "__main__":
    unittest.main()