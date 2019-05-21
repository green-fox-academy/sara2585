from count_letters import CountLetters
import unittest

class testCountLetters(unittest.TestCase):
    def test_counter_letters(self):
        strings = "aannnnnwwee"
        letters = CountLetters(strings)
        self.assertEqual(letters.countLetters(), {"a":2, "n":5, "w":2, "e":2})

    def test_counter_letters_with_emptystrings(self):
        strings = ""
        letters = CountLetters(strings)
        self.assertEqual(letters.countLetters(), {})

    def test_counter_letters_with_None(self):
        strings = None
        letters = CountLetters(strings)
        self.assertEqual(letters.countLetters(), {})
    
    def tearDown(self):
        print("is done")

if __name__ == "__main__":
    unittest.main()