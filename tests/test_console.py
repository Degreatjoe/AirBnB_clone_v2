#!/usr/bin/python3
""" test casses for the console """
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommandCreate(unittest.TestCase):
    """Test cases for the create command with parameters in HBNBCommand"""

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_with_params(self, mock_stdout):
        """Test create command with parameters"""
        with patch('sys.stdin', StringIO('create User name="John_Doe" \
                                         age=30 height=6.2\n')):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertTrue(len(output) > 0)  # Ensuring an ID is printed

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_with_invalid_params(self, mock_stdout):
        """Test create command with invalid parameters"""
        with patch('sys.stdin', StringIO('create User name="John_Doe" \
                                         invalid_param="invalid"\n')):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertTrue(len(output) > 0)  # Ensuring an ID is printed


if __name__ == '__main__':
    unittest.main()
