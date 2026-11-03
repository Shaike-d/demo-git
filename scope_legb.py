# practic 1

# השורה האחרונה תעיף שגיאה שהמשתנה masage לא נמצא\
# הסיבה שהוא משתנה מקומי ואין גישה אליו מהמרחב הגלובלי

# def welcome(name):
#     message = "Welcome " + name
#     return message
# print(welcome("Dana"))
# print(welcome("Dana"))


# practic 2

# יודפס
# 1: local in first
# לא נמצא ןהסיבה: בגלל שהוא משתנה גלובלי והיא אפשר לקרוא לו בפונקציה x שגיאה שהמשתנה 


# practic 3

# רצה שגיאה בגלל שcount הוא משתנה גלובלי
# וכעת בcount המקומי לא שייך בזמן היצירה שלו לומר שהוא שווה את עצמו ועוד משהו.

# תיקון הפונקציה:
# count = 0
# def add_one(count):
#     return count + 1
# print(add_one(count))


# practic 4 
# המשתמש לקח אובייקט שמור בפיתון והשים אותו כמשתנה ולכן בשורה השניה כשהוא החליט להפעיל את האובייקט פיתון מעלה שגיאה שהיא אפשרל קרוא (list) כאובייקט

# practic 5

def add(cart, total, price):
    new_cart =cart + [price]
    new_total = total + price
    return new_cart, new_total

cart = []
total = 0

cart, total = add(cart, total, 100)
cart, total = add(cart, total, 50)

print(cart, total)


