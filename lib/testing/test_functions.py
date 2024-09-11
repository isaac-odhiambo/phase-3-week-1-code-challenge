import unittest
from init.functions import (
    add_numbers, is_even, reverse_string, count_vowels, 
    calculate_factorial, apply_decorator, sort_by_age, merge_dicts
)

class TestFunctions(unittest.TestCase):
    
    def test_add_numbers(self):
        self.assertEqual(add_numbers(3, 5), 8)
        self.assertEqual(add_numbers(-1, 1), 0)

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))
    
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")
    
    def test_count_vowels(self):
        self.assertEqual(count_vowels("Hello World"), 3)
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("bcdfg"), 0)
    
    def test_calculate_factorial(self):
        self.assertEqual(calculate_factorial(5), 120)
        self.assertEqual(calculate_factorial(0), 1)
        self.assertEqual(calculate_factorial(1), 1)
    
    def test_apply_decorator(self):
        @apply_decorator
        def sample_func():
            return "Original Function"
        
        with self.assertLogs() as captured:
            result = sample_func()
            self.assertIn("Decorator Applied", captured.output[0])
            self.assertEqual(result, "Original Function")
    
    def test_sort_by_age(self):
        people = [('Alice', 30), ('Bob', 25), ('Charlie', 35)]
        sorted_people = [('Bob', 25), ('Alice', 30), ('Charlie', 35)]
        self.assertEqual(sort_by_age(people), sorted_people)

    def test_merge_dicts(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        merged = {'a': 1, 'b': 5, 'c': 4}
        self.assertEqual(merge_dicts(dict1, dict2), merged)

if __name__ == '__main__':
    unittest.main()
