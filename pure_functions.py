# practic 1

# def square(n):
# return n * n
# פונקציה טהורה


def log_square(n):
    print("squaring", n)
    return n * n
# פונקציה טהורה

def add_item(cart, item):
    cart.append(item)
    return cart


def with_item(cart, item):
    return cart + [item]

# הפונקציה טהורה


# practic 2


def add_to_total(total,price):
    return total + price

total = 0
total = add_to_total(total, 10)
total = add_to_total(total, 10)
print(total)
print(add_to_total(0, 10))
print(add_to_total(0, 10))