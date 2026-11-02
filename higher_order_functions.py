# practic 1

# def apply_to_all(numbers, action):
#     nums_return = []
#     for n in numbers:
#         nums_return.append(action(n))
#     return nums_return

# def double(n):
#     return n*2

# def rounde(n):
#     return round(n)

# print(apply_to_all([1, 2, 3], double))
# print(apply_to_all([1, 2, 3], lambda n: n * n))
# print(apply_to_all([1.6, 2.4], rounde))



# practic 2

prices = [20, 75, 120, 45, 90]

over_50 = list(filter(lambda p: p>50 , prices))

new_price = list(map(lambda p: p+10 , over_50 ))

print(over_50)
print(new_price)


