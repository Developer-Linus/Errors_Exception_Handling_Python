# Errors and Exception Handling in Python
- In programming, errors are inevitable. In Python, errors can be classified as:
(a) **Syntax errors**: Occur due to violation of Python's grammar rules. The program will not run at all because they're flagged during compilation phase. <br>
(b) **Exceptions errors**: Are runtime errors during program execution that arise during program execution. They indicate unexpected situations that the program encounters. Exceptions allow you to write code that can gracefully handle these situations and prevent program crashes. This type of error occurs whenever **syntactically** correct Python code results in an error.
## Understanding Python Errors
### (a) Common Syntax Errors
- missing colons (:) after statements.
- Incorrect indentation (Python relies on indentation for code blocks).
- Unmatched paranthesis or brackets.
- Typos in variable or function names.
### (b) Common Exceptions
1. **NameError**: occurs when a variable is used before it is defined. <br>
2. **TypeError**: Raised when an operation is attempted on incompatible dat types. <br>
3. **IndexError**: Thrown when trying to access an element outside the list or sequence's index range. <br>
4. **ZeroDivisonError**: Occurs when attempting to divide by zero. <br>
5. **ValueError**: Indicates an inappropriate value passed to a function or operation.

## Mastering Exception Handling
- Exception handling is a powerful Python mechanism to manage errors. 
- The fundamental structure involves `try`, `except`, `else`, and `finally` block.

```
try:
    #code that might raise an exception
except ExceptionType:
    #code to handle exception
else:
    #code that executes if no exception occurs.
finally:
    #code that always executes, regardless of exceptions
```
- You can have multiple exception blocks to handle different exception type. 
- **finally** block is commonly used for cleaning up resources like closing files and releasing databases.
- You can also use the `raise` statement to explicitly raise an exception when encountering an error condition within your code:
```
def divide(x,y):
    if y==0:
        raise ZeroDivisionError("Division by zero is not allowed.")
        return x/y
```
## Custom Exceptions
- user-defined exception classes that you create to handle specific errors or exceptional situations in your code.
##### Benefits
- specific error handling.
- clarity and readability.
- Modularity.
### Creating Custom Exceptions
- Define a new class that inherits from the base exception class or its subclasses (e.g, ValueError, TypeError, etc).
- Optionally, you can add custom attributes or methods to your exception class based on your requirements. 

For large applications, the best practice is to place custom exceptions in a separate module (file). This improves code organization, reusability, and maintainability. Here's a detailed explanation and examples:

## Why Place Custom Exceptions in a Separate File?
- Modularity: Keeps your codebase organized by separating concerns.
- Reusability: Other modules in your application can import the exceptions easily.
- Scalability: As your application grows, managing exceptions becomes easier.

# Practice Exercises
## Exercise 1: Handling ZeroDivisionError
### Instructions:
    • Write a program that takes two numbers as input from the user and divides the first number by the second number.
    • Handle the ZeroDivisionError exception to inform the user if they attempt to divide by zero.
## Exercise 2: File Handling with FileNotFoundError
### Instructions:
    • Write a program that attempts to open and read data from a file specified by the user.
    • Handle the FileNotFoundError exception to provide a meaningful message if the file does not exist.
## Exercise 3: Custom Exception
### Instructions:
    • Create a custom exception class called ValueTooHighError that inherits from the Exception class.
    • Write a program that takes a number as input and raises a ValueTooHighError exception if the number is greater than 100.
