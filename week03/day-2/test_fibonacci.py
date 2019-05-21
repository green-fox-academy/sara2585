import unittest
from fibonacci import Fibonacci

class testFibonacci(unittest.TestCase):
    def test_findFibonacci(self):
        fibonacci = Fibonacci()
        self.assertEqual(fibonacci.findFibonacci(8), 21)

    def test_findFibonacci_with_negative_number(self):
        fibonacci = Fibonacci()
        self.assertEqual(fibonacci.findFibonacci(-1), "The given number is not a index")

    def test_findFibonacci_with_float(self):
        fibonacci = Fibonacci()
        self.assertEqual(fibonacci.findFibonacci(5.5), "The given number is not a index")

    def test_findFibonacci_with_None(self):
        fibonacci = Fibonacci()
        #self.assertEqual(fibonacci.findFibonacci( ), "The given number is not a index")
        with self.assertRaises(TypeError):
            fibonacci.findFibonacci( )


  

    def tearDown(self):
        print("Ok")

if __name__ == "__main__":
    unittest.main()
