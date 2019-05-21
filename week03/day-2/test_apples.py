import unittest
from apples import Apple

class test_Apples(unittest.TestCase):
    def test_get_apple(self):
        apple = Apple()
        self.assertEqual(apple.get_apple(), "Apple")
    def tearDown(self):
        print("it was done")

if __name__ == "__main__":
    unittest.main()
        