# phase-3-week-1-code-challenge
This project contains implementations of various Python functions and a class. Below is a description of each function and class, explaining what it does.

# 1. functions.py
This file contains multiple utility functions for common operations, including arithmetic, string manipulation, list sorting, and dictionary merging.

Function: add_numbers(num1, num2)
Purpose: Returns the sum of two numbers.
Parameters:
num1: The first number.
num2: The second number.
# Example:
python
Copy code
add_numbers(3, 5) # Returns 8
Function: is_even(number)
Purpose: Checks if a number is even.
Parameters:
number: The number to check.
Returns: True if the number is even, otherwise False.
# Example:
python
Copy code
is_even(4) # Returns True
Function: reverse_string(text)
Purpose: Reverses a given string.
Parameters:
text: The string to reverse.
Returns: The reversed string.
Example:
python
#
reverse_string("hello") # Returns "olleh"
# Function: count_vowels(text)
Purpose: Counts the number of vowels (a, e, i, o, u, case-insensitive) in a given string.
Parameters:
text: The string in which to count vowels.
Returns: The total count of vowels.
Example:
python
count_vowels("Hello World") # Returns 3
# Function: calculate_factorial(n)
Purpose: Calculates the factorial of a non-negative integer.
Parameters:
n: The integer for which to calculate the factorial.
Returns: The factorial of n.
Example:
python
Copy code
calculate_factorial(5) # Returns 120 (5 * 4 * 3 * 2 * 1)
# Function: apply_decorator(func)
Purpose: Applies a decorator to a function, printing "Decorator Applied" before calling the original function.
Parameters:
func: The function to decorate.
Returns: The decorated function.
Example:
python

def example_function():
    print("Original function")

decorated_function = apply_decorator(example_function)
decorated_function() 
# Prints:
# "Decorator Applied"
# "Original function"
Function: sort_by_age(people)
Purpose: Sorts a list of tuples by the second element (age) in ascending order.
Parameters:
people: A list of tuples, where each tuple contains a name and an age (e.g., ('Alice', 30)).
Returns: The sorted list of tuples by age.
Example:
python
Copy code
people = [('Alice', 30), ('Bob', 25), ('Charlie', 35)]
sort_by_age(people) 
# Returns [('Bob', 25), ('Alice', 30), ('Charlie', 35)]
# Function: merge_dicts(dict1, dict2)
Purpose: Merges two dictionaries. If they have common keys, their values are summed up.
Parameters:
dict1: The first dictionary.
dict2: The second dictionary.
Returns: A new dictionary with merged values.
Example:
python

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merge_dicts(dict1, dict2) 
# Returns {'a': 1, 'b': 5, 'c': 4}
# 2. oop_car.py
This file contains an example of object-oriented programming (OOP) using a Car class.

Class: Car
Attributes:
make: The manufacturer of the car (e.g., Toyota).
model: The model of the car (e.g., Camry).
year: The manufacturing year of the car (e.g., 2020).
# Method: display_info()
Purpose: Displays the car's information (make, model, and year) in a formatted string.
Example:
python

my_car = Car('Toyota', 'Camry', 2020)
my_car.display_info() 
# Prints "Car Make: Toyota, Model: Camry, Year: 2020"
How to Use This Project
Clone the repository or download the files functions.py and oop_car.py.
Import any of the functions or classes into your Python script.
Example of using a function:
python

from functions import add_numbers
print(add_numbers(5, 10)) # Output: 15
Example of using a class:
python

from oop_car import Car
my_car = Car('Tesla', 'Model 3', 2022)
my_car.display_info() # Output: "Car Make: Tesla, Model: Model 3, Year: 2022"
# Dependencies
No external dependencies required. This project only uses built-in Python libraries.
## Author
This project was developed as part of a Python programming challenge. All functions are implemented with simplicity and efficiency in mind.