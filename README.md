
## Introduction

The goal of this coursework is to develop a Python application for converting between Roman and Decimal numbers. The application serves as a tool for users to seamlessly convert numbers between these two numeral systems. To run the program, ensure Python is installed on your system, then execute the `converter.py` script. Using the program involves choosing the conversion type (Roman to Decimal or Decimal to Roman) and providing the input accordingly.
  Execution guide:
  1) Download the file (converter.py) to your computer.
  2) Open command prompt or terminal.
  3) Navigate to the Directory Containing the Script: 'cd C:\Users\dziug\Downloads'.
  4) Run the Script: 'python converter.py'.
  5) Follow the displayed instructions.

## Body/Analysis

The program implements the Roman-Decimal conversion functionalities using object-oriented programming principles and design patterns. Below are the key aspects of the implementation:

- **Object-Oriented Programming Pillars**: The program incorporates all four pillars of OOP, including polymorphism, abstraction, inheritance, and encapsulation.
- **Design Pattern**: The Factory Method design pattern is utilized to dynamically create converter objects based on the specified conversion type.
- **Unit Tests**: Core functionalities are covered with unit tests using the `unittest` framework, ensuring the correctness of the conversion logic.

- **OOP uses and explanation**:

Polymorphism
Explanation: The convert method is defined in the Converter base class and is overridden by RomanToDecimalConverter and DecimalToRomanConverter subclasses. This allows the same method name to be used for different types of conversions.

Code Example from the Script:

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
Abstraction
Explanation: The Converter class serves as an abstract base class with the convert method defined but not implemented. This hides the details of the conversion process and provides a simple interface for converting numbers.

Code Example from the Script:

class Converter:
    def convert(self, input_value):
        pass
Inheritance
Explanation: The RomanToDecimalConverter and DecimalToRomanConverter classes inherit from the Converter base class. This means they inherit the convert method signature and are required to provide their own implementation.

Code Example from the Script:

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
Encapsulation
Explanation: The conversion logic is encapsulated within the RomanToDecimalConverter and DecimalToRomanConverter classes. This hides the internal implementation details from the user and exposes only the convert method.

Code Example from the Script:

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
        
These examples show how each OOP principle is implemented in the code you wrote. By using these specific examples, you can effectively explain the concepts to your teacher and demonstrate your understanding of OOP principles in Python.


## Results

- The program successfully implements conversion logic for both Roman to Decimal and Decimal to Roman functionalities.
- Challenges faced during implementation primarily revolved around ensuring accurate conversion logic, handling edge cases, and maintaining adherence to PEP8 style guidelines.

## Conclusions

In conclusion, this coursework project has achieved its objectives of developing a robust Roman-Decimal converter in Python. The program demonstrates effective utilization of object-oriented programming principles and design patterns, ensuring modularity and extensibility. Future prospects include potential enhancements such as adding support for additional numeral systems, optimizing conversion algorithms further, and expanding unit test coverage.


Džiugas Sakalauskas Ef-23/2
