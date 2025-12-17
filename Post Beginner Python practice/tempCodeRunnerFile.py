def find_min(numbers):
    if not numbers:
        return None
    minimum = numbers[0]
    for i in numbers:
        if i < minimum:
            minimum = i
    return minimum

nums = [1, 0, 2, 5, 10]
result = find_min(nums)
print(result)
