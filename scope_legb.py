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
count = 0
def add_one(count):
    return count + 1

print(add_one(count))

