import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        test_data1 = CsvReader('/src/Addition.csv').data
        for row in test_data1:
            self.assertEqual(self.calculator.add(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_sub_method_calculator(self):
        test_data2 = CsvReader('/src/Subtraction.csv').data
        for row in test_data2:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_mult_method_calculator(self):

       self.assertEqual(self.calculator.multiply(3,3),9)
       self.assertEqual(self.calculator.result,9)

    def test_div_method_calculator(self):
        self.assertEqual(self.calculator.divide(3,3),1)
        self.assertEqual(self.calculator.result,1)

    def test_squared_method_calculator(self):
        self.assertEqual(self.calculator.doubled(3),9)
        self.assertEqual(self.calculator.result,9)

    def test_root_method_calculator(self):
        self.assertEqual(self.calculator.sq_root(9),3)
        self.assertEqual(self.calculator.result,3)
        
if __name__ == '__main__':
    unittest.main()
