import unittest
from Calculator import Calculator

class MyTestCase(unittest.TestCase):
    #def test_something(self):

    def test_instantiate_calculator(self):
        calculator=Calculator()
        self.assertIsInstance(calculator, Calculator)

        #self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
