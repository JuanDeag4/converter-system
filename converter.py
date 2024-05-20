# converter.py

class Converter:
    def convert(self, input_value):
        pass

class RomanToDecimalConverter(Converter):
    def convert(self, roman_number):
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0
        for char in roman_number[::-1]:
            value = roman_numerals[char]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
        return result

class DecimalToRomanConverter(Converter):
    def convert(self, decimal_number):
        roman_numerals = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        result = ''
        for value, numeral in roman_numerals.items():
            while decimal_number >= value:
                result += numeral
                decimal_number -= value
        return result

class ConverterFactory:
    @staticmethod
    def create_converter(conversion_type):
        if conversion_type == 'roman_to_decimal':
            return RomanToDecimalConverter()
        elif conversion_type == 'decimal_to_roman':
            return DecimalToRomanConverter()
        else:
            raise ValueError("Invalid conversion type")

# Unit tests
import unittest

class TestConverter(unittest.TestCase):
    def test_roman_to_decimal_conversion(self):
        converter = ConverterFactory.create_converter('roman_to_decimal')
        self.assertEqual(converter.convert('X'), 10)
        self.assertEqual(converter.convert('IV'), 4)
    
    def test_decimal_to_roman_conversion(self):
        converter = ConverterFactory.create_converter('decimal_to_roman')
        self.assertEqual(converter.convert(10), 'X')
        self.assertEqual(converter.convert(4), 'IV')

if __name__ == '__main__':
    unittest.main()
