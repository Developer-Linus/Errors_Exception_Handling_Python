# Define custom exceptions
class OutOfStockError(Exception):
    '''Custom exception for handling out-of-stock items.'''
    def __init__(self, item_name):
        self.item_name = item_name
    def __str__(self):
        return f"Sorry, the item {self.item_name} is out of stock"

# Sample Product inventory
product = {
    "apple": 10,
    "banana": 5,
    "orange": 0, # Out of stock
    "grapes": 3
}

'''
Custom Exception OutOfStockError:
    • We define a custom exception class OutOfStockError that inherits from the base Exception class. This custom exception is designed to handle out-of-stock items.
    • The __init__ method initializes the exception with the name of the out-of-stock item.
    • The __str__ method specifies the error message to be displayed when the exception is raised.
Sample Product Inventory:
    • We have a dictionary product_inventory that represents the available quantity of various items in our inventory.
'''

        