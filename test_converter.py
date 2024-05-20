# test_converter.py

import unittest
from converter import ConverterFactory

class TestConverter(unittest.TestCase):
    def test_roman_to_decimal_conversion(self):
        converter = ConverterFactory.create_converter('roman_to_decimal')
        self.assertEqual(converter.convert('I'), 1)
        self.assertEqual(converter.convert('IV'), 4)
        self.assertEqual(converter.convert('X'), 10)
        self.assertEqual(converter.convert('XLII'), 42)
        self.assertEqual(converter.convert('XCIX'), 99)
        self.assertEqual(converter.convert('MMXXIV'), 2024)
    
    def test_decimal_to_roman_conversion(self):
        converter = ConverterFactory.create_converter('decimal_to_roman')
        self.assertEqual(converter.convert(1), 'I')
        self.assertEqual(converter.convert(4), 'IV')
        self.assertEqual(converter.convert(10), 'X')
        self.assertEqual(converter.convert(42), 'XLII')
        self.assertEqual(converter.convert(99), 'XCIX')
        self.assertEqual(converter.convert(2024), 'MMXXIV')

if __name__ == '__main__':
    unittest.main()
