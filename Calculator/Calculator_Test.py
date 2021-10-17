import unittest


class TestSearchusers(unittest.TestCase):
    def test_add(self):
        '''Sets the memory to 0 and tests add method by adding the integer 10.'''
        calculator.set_memory(0)
        calculator.add(10)
        result = calculator.get_result()
        self.assertEqual(result, 10)

    def test_subtract(self):
        '''Sets the memory to 12 and tests subtract method by subtracting the integer 2.'''
        calculator.set_memory(12)
        calculator.sub(2)
        result = calculator.get_result()
        self.assertEqual(result, 10)

    def test_multiply(self):
        '''Sets the memory to 9 and tests multiply method by multipling by integer 2.'''
        calculator.set_memory(9)
        calculator.mult(2)
        result = calculator.get_result()
        self.assertEqual(result, 18)

    def test_divide(self):
        '''Sets the memory to 40 and tests divide method by dividing by integer 10.'''
        calculator.set_memory(40)
        calculator.div(10)
        result = calculator.get_result()
        self.assertEqual(result, 4)

    def test_root(self):
        '''Sets the memory to 20 and tests root method by taking the root 2.'''
        calculator.set_memory(20)
        calculator.root(2)
        result = calculator.get_result()
        self.assertEqual(result, 4.47213595499958)


if __name__ == '__main__':

    from Calculator.Calculator_Class import Calculator

    calculator = Calculator(memory = 0)

    unittest.main()
