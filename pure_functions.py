# practic 1

# def square(n):
# return n * n
# פונקציה טהורה


# def log_square(n):
#     print("squaring", n)
#     return n * n
# # פונקציה טהורה

# def add_item(cart, item):
#     cart.append(item)
#     return cart


# def with_item(cart, item):
#     return cart + [item]

# # הפונקציה טהורה


# # practic 2
# def add_to_total(total,price):
#     return total + price


# # practic 3
# def apply_tax(prices):
#     tax_price = []
#     for price in prices:
#         price *= 1.17
        
#         tax_price.append(price)
#     return tax_price

# prices = [100, 50]
# with_tax = apply_tax(prices)
# print(prices)
# print(with_tax)


# practic 4

# def calculate_total(prices):
#     total = 0
#     for price in prices:
#         total = total + price
#     return total
    
# def show_total(prices):
#     total = calculate_total(prices)
#     print("Total:",total)

# show_total([10, 20, 30])


# practic 5

def top_three(numbers):
    copy_list = numbers.copy()
    copy_list.sort()
    top_three = copy_list[0:3]
    return top_three
    

scores = [70, 95, 88, 60, 99]
print(top_three(scores))
print(scores)