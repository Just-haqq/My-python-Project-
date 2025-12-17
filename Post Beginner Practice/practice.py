print("Hello world")

#addition
num1 = float(input("Ener your first number "))
num2 = float(input("Enter your second number "))
Aresult = num1 + num2
print(f'Your answer is {Aresult}')

#Division
try: 
    number1 = float(input('Your first number: '))
    number2 = float(input("Your second number: "))
    Dresult = number1 / number2
    print(f"Your answer is {Dresult}")
except ZeroDivisionError:
    print("Sorry, Second number can't be Zero")

except ValueError:
    print("Invalid Value!")


#Area Of a Triangle
Base = float(input("Base= ") )
Height = float(input("Height= "))
area = Base * Height
print(f"Area is {area} ")

#Swapping the values of two numbers
numb1 = float(input("a = "))
numb2 = float(input("b = "))
temp = numb1
numb1 = numb2
numb2 = temp
print(f" a = {numb1} , b= {numb2}")


#Generating Random numbers
import random
print(f'Your lucky number is {random.randint(1, 100)}')


#Convert kilometers to meters and vise-versa
value = float(input("number: ") )
variable = input("Is the value in Km or M: ").lower()
if variable == 'km':
    meters = 1000 * value
    print(f"{meters}m")
elif variable == 'm':
    kilometers = value / 1000
    print(f"{kilometers}km")
else:print("invalid variable")


#Convert between Fahrenheit and celcius
number = float(input("number: "))
degree = input("Is the value in F or C: ").upper()
if degree == 'C':
    fahrenheit = (number * 9/5) + 32
    print(f'{fahrenheit} degree Fahrenheit')
elif degree == 'F':
    Celcius = (number - 32) * 5/9
    print(f'{Celcius} degree Celcius')
else:
    print('Invalid Degree Scope')


#Calendar
import calendar

year = int(input ("What year were you born? "))
month = int(input("What is your birth month? "))

cal = calendar.month(year, month)
print(cal)


# Quadratic Equation
import math
a = float(input("What is the value of a? "))
b = float(input("What is the value of b? "))
c = float(input("What is the value of c? "))

discriminant = b**2 - 4 * a * c

if discriminant > 0:
    root1 = -b + math.sqrt(discriminant)
    root2 = -b - math.sqrt(discriminant)
    print(f'root 1 = {root1}')
    print(f'root 2 = {root2}')

elif discriminant == 0:
    root = -b / (2 * a)
    print(f'root = {root}')

else:
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
    print(f'Root 1 = {real_part} + {imaginary_part}i')
    print(f'Root 2 = {real_part} - {imaginary_part}i')


#leap year check

year = int(input("Enter a year? "))

if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
    

elif (year % 4 == 0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

else:
    print("{0} is not a leap year".format(year))



#Prime number check
num = int(input("Enter your number "))

flag = False

if num == 1:
    print("Number is not a prime number ")

elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            
            break

if flag:
    print(f"{num} is not a prime number")

else:
    print(f"{num} is a prime number ")

class Mammal():
    def walk(self):
        print("Walk")
    
cat = Mammal
cat.walk

#Fibonacci Sequence

nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0

if nterms < 0:
    print("Term number cannot be negative")

elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)

else:
    print('Fibonacci sequence: ')
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    
num = int(input('Enter a number:'))
num_length = len(str(num))
temp = num 
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit**num_length
    temp = temp // 10

if total == num:
    print(f'{num},is an Armstrong number')
else :
    print(f'{num}, is not an Armstrong number')


limit = int(input('Enter limit: '))
sum = 0

for i in range(1, limit + 1):
    sum += i

print(f'The sum of natural number up to {limit} is {sum}')


#simple calculator

def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


print(""" select option.
      1. Addition
      2. Subtraction
      3. Multiplication
      4. Division
      """ )

while True:
    choice = input("Please choose your option:(1 / 2 / 3/ 4) ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print('Invalid option')
    
    if choice == '1':
        print(num1, '+', num2, '=', addition(num1, num2) )
    
    elif choice == '2':
        print(num1, '-', num2, '=', subtraction(num1, num2))
    
    elif choice == '3':
        print(num1, '*', num2, '=', multiplication(num1, num2))
    
    elif choice == '4':
        print(num1, '/', num2, '=', division(num1, num2))
    
    next_calcularion = input('Do another calculation?(yes/no) ').lower()
    
    if next_calcularion == "no":
        break

else:
    print("invalid input")



def find_min(numbers):
    if not numbers:
        return None
    min = number[0]
    