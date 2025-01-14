# Define the custom exception
class ValueTooHighError(Exception):
    def __init__(self, number):
        self.number = number
    def __str__(self):
        return f"'{self.number}' is too high."

# Function to check the number
def num_checking(number):
    try:
        if number <= 100:
            return f"{number} is safe to work with. Proceed."
        else:
            # Raise the custom exception for numbers greater than 100
            raise ValueTooHighError(number)
    except TypeError as e:
        print(e)

# User interaction
number = int(input("Enter the number to check: "))
try:
    result = num_checking(number)
    print(result)
except ValueTooHighError as e:
    print(e)
