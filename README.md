# Errors and Exception Handling in Python
- In programming, errors are inevitable. In Python, errors can be classified as:
(a) **Syntax errors**: Occur due to violation of Python's grammar rules. The program will not run at all because they're flagged during compilation phase. <br>
(b) **Exceptions errors**: Are runtime errors during program execution that arise during program execution. They indicate unexpected situations that the program encounters. Exceptions allow you to write code that can gracefully handle these situations and prevent program crashes. 
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