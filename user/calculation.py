# calculation.py

def calculate_tax(subtotal):
    # Assuming tax rate is 5%
    tax_rate = 0.05
    return subtotal * tax_rate

def calculate_shipping(subtotal):
    # Assuming shipping cost is $15
    shipping_cost = 15
    return shipping_cost

# user/calculation.py

def calculate_subtotal(cart):
    subtotal = 0
    for item in cart:
        price = float(item['price'])  # Convert price to float
        quantity = int(item['quantity'])  # Convert quantity to integer
        subtotal += price * quantity
    return subtotal
