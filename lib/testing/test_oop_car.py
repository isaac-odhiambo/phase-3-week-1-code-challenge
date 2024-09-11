import unittest
from io import StringIO
import sys
from init.car import Car

class TestCar(unittest.TestCase):
    
    def test_car_initialization(self):
        car = Car('Toyota', 'Camry', 2020)
        self.assertEqual(car.make, 'Toyota')
        self.assertEqual(car.model, 'Camry')
        self.assertEqual(car.year, 2020)

    def test_display_info(self):
        car = Car('Honda', 'Civic', 2019)
        captured_output = StringIO()
        sys.stdout = captured_output  # Redirect stdout
        car.display_info()
        sys.stdout = sys.__stdout__  # Reset redirect
        
        self.assertEqual(captured_output.getvalue().strip(), "Car Make: Honda, Model: Civic, Year: 2019")

if __name__ == '__main__':
    unittest.main()
