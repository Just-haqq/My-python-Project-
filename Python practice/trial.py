# simple calculator

def addition(x,y):
    return x + y

def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

print(""" please select from these options only
      1. Addition
      2. Subtraction
      3. Multiplication
      4. Division
      """)

while True:
    choice = input(" Please choose (1 / 2 / 3 / 4): ")
    
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print('Invalid! ')
    
    if choice == '1':
        print(num1, '+', num2, '=', addition(num1, num2))
    
    elif choice == '2':
        print(num1, '-', num2, '=', subtraction(num1, num2))
    
    elif choice == '3':
        print(num1, '*', num2, '=', multiplication(num1, num2) )
    
    elif choice == '4':
        print(num1, '/', num2, '=', division(num1, num2))

    another = input('Will you make another calculation? (yes/no) ').lower()
    
    if another == 'no':
        break
else:
    print('Invalid Value')


#Random number guessing game
import random
start = int(input('Enter the lower starting Number: '))
end = int(input("Enter the higher end Number: "))
random_number = random.randint(start, end)
guess_count = 0
tries = 7
while guess_count < tries:
    guess_count = guess_count + 1
    guess = int(input("Enter the number: "))
    if guess == random_number:
        print("Correct!")
        break
    elif guess < random_number:
        print("Too low")
    elif guess > random_number:
        print("Too high!")
    elif guess_count > tries and guess != random_number:
        print("You have exhausted your tries ")

