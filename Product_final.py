# Name: Maria Bano , Reg: sp23-bai-025
# Name: Ahmed Hussain , Reg: sp23-bai-007
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

    def make_purchase(self, quantity):
        # Handle the purchase process, update stock, and return the total cost
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if quantity > self.amount:
            raise ValueError(f"Cannot purchase {quantity} units. Only {self.amount} left in stock.")
        
        total_cost = self.get_price(quantity)
        self.amount -= quantity  # Update stock after purchase
        print(f"Purchased {quantity} units of {self.name} for ${total_cost:.2f}")
        print(f"Remaining stock: {self.amount} units")
        return total_cost
# Test the Product class
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
