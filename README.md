# converter-system
Got it! Let's draft the report based on these requirements:

---

# Coursework Report: Roman-Decimal Converter

## Introduction

The goal of this coursework is to develop a Python application for converting between Roman and Decimal numbers. The application serves as a tool for users to seamlessly convert numbers between these two numeral systems. To run the program, ensure Python is installed on your system, then execute the `converter.py` script. Using the program involves invoking the appropriate conversion functions, providing either Roman numerals or integers as input.

## Body/Analysis

The program's implementation revolves around object-oriented programming principles and design patterns to ensure modularity, extensibility, and maintainability. Below are the key aspects of the implementation:

- **Polymorphism**: Achieved through method overriding in subclass implementations of the `convert` method.
- **Abstraction**: Each class encapsulates the conversion logic, abstracting away implementation details.
- **Inheritance**: Subclasses (`RomanToDecimalConverter` and `DecimalToRomanConverter`) inherit from the base class `Converter`, promoting code reuse.
- **Encapsulation**: Data and methods are encapsulated within classes, providing better control over access and modification.

To meet the functional requirements, the program utilizes the Factory Method design pattern to create converter objects dynamically. This pattern allows for the creation of converter objects without specifying their exact types, enhancing flexibility and scalability.

## Results

- Successful implementation of conversion logic for both Roman to Decimal and Decimal to Roman functionalities.
- Challenges faced during implementation primarily revolved around ensuring accurate conversion logic, handling edge cases, and maintaining adherence to PEP8 style guidelines.

## Conclusions

In conclusion, this coursework project has achieved its objectives of developing a robust Roman-Decimal converter in Python. The program demonstrates effective utilization of object-oriented programming principles and design patterns, ensuring modularity and extensibility. Future prospects include potential enhancements such as adding support for additional numeral systems, optimizing conversion algorithms further, and expanding unit test coverage.
