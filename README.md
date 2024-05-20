
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

Code snippets from the program are provided to illustrate the implementation of the requirements.

## Results

- The program successfully implements conversion logic for both Roman to Decimal and Decimal to Roman functionalities.
- Challenges faced during implementation primarily revolved around ensuring accurate conversion logic, handling edge cases, and maintaining adherence to PEP8 style guidelines.

## Conclusions

In conclusion, this coursework project has achieved its objectives of developing a robust Roman-Decimal converter in Python. The program demonstrates effective utilization of object-oriented programming principles and design patterns, ensuring modularity and extensibility. Future prospects include potential enhancements such as adding support for additional numeral systems, optimizing conversion algorithms further, and expanding unit test coverage.

1. Polymorphism
Definition: Polymorphism allows objects of different classes to be treated as objects of a common superclass. It provides a way to perform a single action in different forms.

Explanation: In the converter program, polymorphism is achieved through the Converter base class and its subclasses (RomanToDecimalConverter and DecimalToRomanConverter). Each subclass implements the convert method, but the implementation details differ based on the type of conversion.

Code Example:

python
Copy code
class Converter:
    def convert(self, input_value):
        pass

class RomanToDecimalConverter(Converter):
    def convert(self, roman_number):
        # Implementation for converting Roman to Decimal
        pass

class DecimalToRomanConverter(Converter):
    def convert(self, decimal_number):
        # Implementation for converting Decimal to Roman
        pass
Usage:

python
Copy code
converter = ConverterFactory.create_converter('roman_to_decimal')
print(converter.convert('X'))  # Output: 10

converter = ConverterFactory.create_converter('decimal_to_roman')
print(converter.convert(10))  # Output: X
2. Abstraction
Definition: Abstraction involves hiding the complex implementation details of a system and exposing only the necessary parts. It helps in reducing complexity and allows the programmer to focus on interactions at a higher level.

Explanation: The Converter class acts as an abstract base class with the convert method, which is meant to be overridden by its subclasses. This design hides the complex conversion logic and provides a simple interface for performing conversions.

Code Example:

python
Copy code
class Converter:
    def convert(self, input_value):
        pass
Explanation: The convert method is an abstract method that subclasses must implement, providing a clear and simplified interface for conversion operations.

3. Inheritance
Definition: Inheritance is a mechanism where a new class inherits properties and behavior (methods) from an existing class. It promotes code reusability and establishes a relationship between classes.

Explanation: In the converter program, RomanToDecimalConverter and DecimalToRomanConverter inherit from the Converter base class. This allows them to inherit the convert method signature and ensures that they provide their own implementation of this method.

Code Example:

python
Copy code
class RomanToDecimalConverter(Converter):
    def convert(self, roman_number):
        # Implementation specific to Roman to Decimal conversion
        pass

class DecimalToRomanConverter(Converter):
    def convert(self, decimal_number):
        # Implementation specific to Decimal to Roman conversion
        pass
Explanation: Both RomanToDecimalConverter and DecimalToRomanConverter inherit the convert method from Converter, ensuring a consistent interface.

4. Encapsulation
Definition: Encapsulation is the practice of bundling data (attributes) and methods (functions) that operate on the data into a single unit or class. It restricts direct access to some of the object's components, which can prevent the accidental modification of data.

Explanation: The converter program encapsulates the conversion logic within the RomanToDecimalConverter and DecimalToRomanConverter classes. This means that the internal implementation details are hidden from the user, who interacts only with the public convert method.

Code Example:

python
Copy code
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
Explanation: The conversion logic (e.g., the dictionary of Roman numerals and the calculation algorithm) is encapsulated within the RomanToDecimalConverter class. Users of the class do not need to know the details of this logic; they simply call the convert method.

Conclusion
By incorporating these OOP principles, the Roman-Decimal Converter program ensures that the code is modular, reusable, and easy to understand. The use of polymorphism, abstraction, inheritance, and encapsulation makes the system robust and flexible, allowing for future extensions and modifications with minimal impact on existing functionality.

Džiugas Sakalauskas Ef-23/2
