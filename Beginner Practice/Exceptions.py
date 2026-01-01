try:
    age = int(input("age: "))
    income = 2000
    risk = income/ age
    print(age)
except ZeroDivisionError:
    print("Age cannot be Zero")
except ValueError:
    print('Invalid Value')