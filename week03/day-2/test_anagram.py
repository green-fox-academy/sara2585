from anagram import Anagram
import unittest

class testAnagram(unittest.TestCase):
    def test_is_anagram(self):
        anagram = Anagram()
        self.assertEqual(anagram.is_Anagram("abc", "bca"), True)

    def test_isnot_anagram01(self):
        anagram = Anagram()
        self.assertEqual(anagram.is_Anagram("abc", "bcca"), False)

    def test_is_anagram_with_oneparameter(self):
        anagram = Anagram()
        self.assertEqual(anagram.is_Anagram("", "bcca"), False)

    def tearDown(self):
        print("is done")

if __name__ == "__main__":
    unittest.main()