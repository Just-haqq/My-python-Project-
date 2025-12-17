def find_min(numbers):
    if not numbers:
        return None
    minimum = numbers[0]
    for i in numbers:
        if i < minimum:
            minimum = i
    return minimum

user_input = input('Enter the numbers separated by spaces: ')
numbers = list(map(int, user_input.split()))

result = find_min(numbers)
if None:
    print('List cannot be blank')
else:
    print(f'Minimum number in list in the list is{result}')