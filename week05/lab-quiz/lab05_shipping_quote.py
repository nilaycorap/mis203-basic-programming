
def calculate_subtotal(price, quantity):
    return price * quantity


def get_discount_rate(subtotal):
    if subtotal >= 100:
        return 0.10
    return 0.0


def calculate_shipping(subtotal):
    if subtotal >= 100:
        return 0.0
    return 10.0


def calculate_total(subtotal, discount_rate, shipping_fee):
    discount = subtotal * discount_rate
    return subtotal - discount + shipping_fee


# Test our functions
assert calculate_subtotal(20, 3) == 60
assert get_discount_rate(99.99) == 0.0
assert get_discount_rate(100) == 0.10
assert calculate_shipping(100) == 0.0
assert calculate_total(100, 0.10, 0.0) == 90.0


# Sample orders
orders = [
    {"name": "Order 1", "price": 20.0, "quantity": 3},
    {"name": "Order 2", "price": 25.0, "quantity": 5},
]

for order in orders:
    subtotal = calculate_subtotal(
        order["price"], order["quantity"]
    )
    discount_rate = get_discount_rate(subtotal)
    shipping_fee = calculate_shipping(subtotal)
    total = calculate_total(
        subtotal, discount_rate, shipping_fee
    )

    print(f"\n{order['name']}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: {discount_rate:.0%}")
    print(f"Shipping: ${shipping_fee:.2f}")
    print(f"Final total: ${total:.2f}")

print("\nAll tests passed!")
