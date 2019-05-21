from anagram import Anagram
import unittest

class testAnagram(unittest.TestCase):
    def test_is_anagram(self):
        anagram = Anagram()
        self.assertTrue(anagram.is_Anagram("abc", "bca"))

    def test_isnot_anagram01(self):
        anagram = Anagram()
        self.assertFalse(anagram.is_Anagram("abc", "bcca"))

    def test_is_anagram_with_oneparameter(self):
        anagram = Anagram()
        self.assertFalse(anagram.is_Anagram("", "bcca"))

    def tearDown(self):
        print("is done")

if __name__ == "__main__":
    unittest.main()