def find_min(numbers):
    if not numbers:
        return None
    min = numbers[0]
    for i in numbers:
        if i < min:
            min = i
            break
print(f'The minimum is {min}')
    
num = [0, 1, 2, 3, 4]
find_min(num)