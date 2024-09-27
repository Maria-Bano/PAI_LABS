class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount  # stock quantity
        self.price = price  # price per unit

    def get_price(self, quantity):
        # Return the total price for a given quantity of the product
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        return self.price * quantity

# Test the Product class
try:
    # Creating product
    laptop = Product("Laptop", 10, 1000)

    # Test cases for different quantities
    laptop.make_purchase(2)  # Buy 2 laptops
    laptop.make_purchase(5)  # Buy 5 laptops
    laptop.make_purchase(4)  # Attempt to buy more than stock (should raise an error)
except ValueError as e:
    print(e)

try:
    laptop.make_purchase(-1)  # Invalid quantity test (should raise an error)
except ValueError as e:
    print(e)
