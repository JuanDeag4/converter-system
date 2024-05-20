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



if __name__ == '__main__':
    print("Welcome to the Roman-Decimal Converter!")
    print("Please choose the conversion type:")
    print("1. Roman to Decimal")
    print("2. Decimal to Roman")
    choice = input("Enter your choice (1/2): ")
    if choice == '1':
        roman_input = input("Enter the Roman numeral: ")
        converter = ConverterFactory.create_converter('roman_to_decimal')
        result = converter.convert(roman_input)
        print("Decimal equivalent:", result)
    elif choice == '2':
        decimal_input = int(input("Enter the decimal number: "))
        converter = ConverterFactory.create_converter('decimal_to_roman')
        result = converter.convert(decimal_input)
        print("Roman numeral:", result)
    else:
        print("Invalid choice. Please choose either 1 or 2.")
