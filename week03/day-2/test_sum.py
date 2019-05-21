from sum import mySum
import unittest

class testSum(unittest.TestCase):
    def test_mySum(self):
        numlist = [3,5,9]
        mysum = mySum(numlist)
        self.assertEqual(mysum.Sum(), 17)
    
    def test_mySum_with_emptylist(self):
        mysum = mySum()
        self.assertEqual(mysum.Sum(), 0)
    
    def test_mySum_with_one_num(self):
        numlist = [5]
        mysum = mySum(numlist)
        self.assertEqual(mysum.Sum(), 5)

    def test_mySum_with_None(self):
        numlist = None
        mysum = mySum()
        self.assertEqual(mysum.Sum(), 0)

    def tearDown(self):
        print("all done")

if __name__  == "__main__":
    unittest.main()
    