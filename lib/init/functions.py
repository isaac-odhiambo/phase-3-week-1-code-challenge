# Function: add_numbers
def add_numbers(num1, num2):
    return num1 + num2

# Function: is_even
def is_even(number):
    return number % 2 == 0

# Function: reverse_string
def reverse_string(text):
    return text[::-1]

# Function: count_vowels
def count_vowels(text):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

# Function: calculate_factorial
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

# Function: apply_decorator
def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    return decorator_func(func)

# Sequences: Sort List of Tuples
def sort_by_age(people):
    return sorted(people, key=lambda person: person[1])

# Sets and Dictionaries: Merge Dictionaries
def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged