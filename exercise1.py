# User interaction
x = int(input("Enter the first number (the number to be divided)."))
y = float(input("Enter the second number (the number to divide by)."))

def division_function(x,y):
    return x/y
try:
    print(division_function(x,y))
except ZeroDivisionError:
    print("Division by zero (0) is not allowed.")