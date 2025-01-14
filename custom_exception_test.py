'''
Function purchase_item(item, quantity):
    • This function simulates purchasing items from the inventory.
    • It checks if the requested item is available in the inventory and if it’s in stock. If the item is in stock, it reduces the quantity accordingly.
    • If the item is out of stock, it raises the OutOfStockError custom exception.
'''

import custom_exceptions

# Function to handle purchases
def purchase_item(item, quantity):
    try:
        if custom_exceptions.product[item] == 0:
            raise custom_exceptions.OutOfStockError(item)
        else:
            print(f"Purchase successful: {quantity} {item}(s)")
            custom_exceptions.product[item] -= quantity
    except KeyError:
        print(f"Sorry, '{item}' is not available in our inventory.")

# Testing the Custom Exception
try:
    purchase_item("apple", 3)  # Purchase successful
    purchase_item("orange", 1)  # Raises OutOfStockError
    purchase_item("watermelon", 1)  # Item not available
except custom_exceptions.OutOfStockError as e:
    print(e)

