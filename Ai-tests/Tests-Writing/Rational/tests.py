import unittest
from rational import Rational

class TestRational(unittest.TestCase):
    def setUp(self):
        self.r_positive = Rational(4, 6)
        self.r_negative = Rational(-4, 6)
        self.r_mixed_positive = Rational(7, 3)
        self.r_mixed_negative = Rational(-7, 3)
        self.r_zero = Rational(0, 3)

    def test_constructor(self):
        self.assertEqual(self.r_positive.numerator, 4)
        self.assertEqual(self.r_positive.denominator, 6)
        
        self.assertEqual(self.r_negative.numerator, -4)
        self.assertEqual(self.r_negative.denominator, 6)
        
        with self.assertRaises(ValueError):
            Rational(4, 0)

    def test_str(self):
        self.assertEqual(str(self.r_positive), "4/6")

    def test_reduce(self):
        reduced_r = self.r_positive.reduce()
        self.assertEqual(reduced_r.numerator, 2)
        self.assertEqual(reduced_r.denominator, 3)

    def test_arithmetic_operations(self):
        r1 = self.r_positive
        r2 = Rational(3, 5)
        
        result_add = r1 + r2
        self.assertEqual(result_add.numerator, 19)
        self.assertEqual(result_add.denominator, 15)
        
        result_sub = r1 - r2
        self.assertEqual(result_sub.numerator, 1)
        self.assertEqual(result_sub.denominator, 15)
        
        result_mul = r1 * r2
        self.assertEqual(result_mul.numerator, 2)
        self.assertEqual(result_mul.denominator, 5)
        
        result_div = r1 / r2
        self.assertEqual(result_div.numerator, 10)
        self.assertEqual(result_div.denominator, 9)

    def test_comparison(self):
        r1 = self.r_positive
        r2 = Rational(3, 5)
        
        self.assertTrue(r1 == Rational(4, 6))
        
        self.assertTrue(r2 < r1)
        
        self.assertTrue(r2 <= Rational(3, 5))
        
        self.assertTrue(r1 > Rational(1, 2))
        
        self.assertTrue(r1 >= Rational(4, 6))

    def test_mixed_form(self):
        self.assertEqual(self.r_mixed_positive.mixed_form, "2 1/3")
        self.assertEqual(self.r_mixed_negative.mixed_form, "-2 1/3")
        self.assertEqual(self.r_zero.mixed_form, "0")
        self.assertEqual(Rational(2, 3).mixed_form, "2/3")

    def test_mixed_form_setter(self):
        r = self.r_mixed_positive
        
        r.mixed_form = "2 1/3"
        self.assertEqual(r.numerator, 7)
        self.assertEqual(r.denominator, 3)
        
        r.mixed_form = "-2 1/3"
        self.assertEqual(r.numerator, -7)
        self.assertEqual(r.denominator, 3)

        r.mixed_form = "1/3"
        self.assertEqual(r.numerator, 1)
        self.assertEqual(r.denominator, 3)

if __name__ == "__main__":
    unittest.main()
