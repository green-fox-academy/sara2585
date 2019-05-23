from Sharpie import Sharpie
import unittest

class test_Sharpie(unittest.TestCase):
    def test_sharpie_without_giving_a_ink_amount(self):
        sharpie = Sharpie("red", 50)
        self.assertEqual(sharpie.use(),98)

    def test_sharpie_with_0_ink(self):
        sharpie = Sharpie("red", 10, 0)
        self.assertEqual(sharpie.use(), "It's all used!")

    def test_sharpie_with_negative_ink(self):
        sharpie = Sharpie("blue", 10, -2)
        self.assertEqual(sharpie.use(), "It's all used!")

    def test_sharpie_with_a_float_ink(self):
        sharpie = Sharpie("red", 1, 20.0)
        self.assertEqual(sharpie.use(), 18.0)

    def test_sharpie_with_invalid_ink(self):
        sharpie = Sharpie('blue', 20, "a")
        with self.assertRaises(TypeError):
            sharpie.use()

    def test_sharpie_without_giving_a_width(self):
        with self.assertRaises(TypeError):
            sharpie = Sharpie("red")


if __name__ == "__main__":
    unittest.main()

