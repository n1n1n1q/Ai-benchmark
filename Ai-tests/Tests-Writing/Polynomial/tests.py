import unittest
from polynomial import Mono, Polynomial


class TestMono(unittest.TestCase):

    def test_monomial_creation(self):
        mono = Mono(3, 2)
        self.assertEqual(mono.coefficient, 3)
        self.assertEqual(mono.degree, 2)

    def test_monomial_str_positive_coefficient(self):
        mono = Mono(3, 2)
        self.assertEqual(str(mono), "Mono: 3x**2")

    def test_monomial_str_negative_coefficient(self):
        mono = Mono(-3, 2)
        self.assertEqual(str(mono), "Mono: -3x**2")

    def test_monomial_str_coefficient_one(self):
        mono = Mono(1, 2)
        self.assertEqual(str(mono), "Mono: x**2")

    def test_monomial_str_coefficient_negative_one(self):
        mono = Mono(-1, 2)
        self.assertEqual(str(mono), "Mono: -x**2")

    def test_monomial_repr(self):
        mono = Mono(3, 2)
        self.assertEqual(repr(mono), "Mono(coeff=3, degree=2)")

    def test_monomial_equality(self):
        mono1 = Mono(3, 2)
        mono2 = Mono(3, 2)
        self.assertEqual(mono1, mono2)

    def test_monomial_inequality(self):
        mono1 = Mono(3, 2)
        mono2 = Mono(2, 2)
        self.assertNotEqual(mono1, mono2)

    def test_monomial_eq_different_coefficients(self):
        mono1 = Mono(3, 2)
        mono2 = Mono(4, 2)
        self.assertNotEqual(mono1, mono2)

    def test_monomial_eq_different_degrees(self):
        mono1 = Mono(3, 2)
        mono2 = Mono(3, 3)
        self.assertNotEqual(mono1, mono2)


class TestPolynomial(unittest.TestCase):

    def test_polynomial_creation(self):
        mono1 = Mono(3, 2)
        mono2 = Mono(2, 1)
        polynomial = Polynomial(mono1, mono2)
        self.assertEqual(str(polynomial), "Polynomial: 3x**2+2x")

    def test_polynomial_degree(self):
        mono1 = Mono(3, 2)
        mono2 = Mono(2, 1)
        polynomial = Polynomial(mono1, mono2)
        self.assertEqual(polynomial.degree, 2)

    def test_polynomial_evaluation(self):
        mono1 = Mono(3, 2)
        mono2 = Mono(2, 1)
        polynomial = Polynomial(mono1, mono2)
        self.assertEqual(polynomial.eval_at(2), 16)

    def test_polynomial_addition(self):
        mono1 = Mono(3, 2)
        mono2 = Mono(2, 1)
        polynomial1 = Polynomial(mono1)
        polynomial2 = Polynomial(mono2)
        result = polynomial1 + polynomial2
        self.assertEqual(str(result), "Polynomial: 3x**2+2x")

    def test_polynomial_subtraction(self):
        mono1 = Mono(3, 2)
        mono2 = Mono(2, 1)
        polynomial1 = Polynomial(mono1)
        polynomial2 = Polynomial(mono2)
        result = polynomial1 - polynomial2
        self.assertEqual(str(result), "Polynomial: 3x**2-2x")

    def test_polynomial_multiplication(self):
        mono1 = Mono(3, 2)
        mono2 = Mono(2, 1)
        polynomial1 = Polynomial(mono1, mono2)

        mono3 = Mono(1, 1)
        mono4 = Mono(4, 0)
        polynomial2 = Polynomial(mono3, mono4)

        result = polynomial1 * polynomial2
        self.assertEqual(str(result), "Polynomial: 3x**3+14x**2+8x")

    def test_polynomial_equality(self):
        mono1 = Mono(3, 2)
        mono2 = Mono(2, 1)
        polynomial1 = Polynomial(mono1, mono2)
        polynomial2 = Polynomial(mono1, mono2)
        self.assertEqual(polynomial1, polynomial2)

    def test_polynomial_hashing(self):
        mono1 = Mono(3, 2)
        mono2 = Mono(2, 1)
        polynomial1 = Polynomial(mono1, mono2)
        polynomial2 = Polynomial(mono1, mono2)
        self.assertEqual(hash(polynomial1), hash(polynomial2))

    def test_polynomial_derivative(self):
        mono1 = Mono(3, 2)
        mono2 = Mono(2, 1)
        polynomial = Polynomial(mono1, mono2)
        derivative = polynomial.derivative
        self.assertEqual(str(derivative), "Polynomial: 6x+2")

    def test_polynomial_creation_with_other_polynomials(self):
        mono1 = Mono(3, 2)
        mono2 = Mono(2, 1)
        poly1 = Polynomial(mono1, mono2)

        mono3 = Mono(1, 1)
        mono4 = Mono(4, 0)
        poly2 = Polynomial(mono3, mono4)

        poly = Polynomial(poly1, poly2)
        self.assertEqual(str(poly), "Polynomial: 3x**2+2x+x+4")

    def test_polynomial_single_monomial_with_coefficient_zero(self):
        mono = Mono(0, 0)
        polynomial = Polynomial(mono)
        self.assertEqual(str(polynomial), "Polynomial: 0")

    def test_polynomial_multiple_monomials_with_coefficient_zero(self):
        mono1 = Mono(0, 0)
        mono2 = Mono(0, 1)
        mono3 = Mono(0, 2)
        polynomial = Polynomial(mono1, mono2, mono3)
        self.assertEqual(str(polynomial), "Polynomial: 0")

    def test_polynomial_repr(self):
        mono1 = Mono(3, 2)
        mono2 = Mono(2, 1)
        polynomial = Polynomial(mono1, mono2)
        self.assertEqual(
            repr(polynomial),
            "Polynomial(Mono(coeff=3, degree=2) -> Mono(coeff=2, degree=1))",
        )

    def test_sort_monomials_with_zero_coefficient(self):
        # Create monomials with the same degree but one has a coefficient of 0
        mono1 = Mono(3, 2)
        mono2 = Mono(0, 2)
        mono3 = Mono(2, 2)

        # Create a polynomial with these monomials
        polynomial = Polynomial(
            mono2, mono3, mono1
        )  # Here we intentionally shuffle the order

        # Sort the polynomial
        polynomial.sort()

        # Ensure that the polynomial is sorted correctly
        self.assertEqual(str(polynomial), "Polynomial: 2x**2+3x**2")

    def test_simplify_with_leading_zeros(self):
        # Create monomials with leading zeros
        mono1 = Mono(0, 2)
        mono2 = Mono(0, 1)
        mono3 = Mono(3, 0)
        mono4 = Mono(2, 1)

        # Create a polynomial with these monomials
        polynomial = Polynomial(mono1, mono2, mono3, mono4)

        # Simplify the polynomial
        polynomial.simplify()

        # Ensure that the polynomial is simplified correctly
        self.assertEqual(str(polynomial), "Polynomial: 3+2x")

    def test_simplify_to_zero_polynomial(self):
        # Create monomials
        mono1 = Mono(2, 2)
        mono2 = Mono(-2, 2)

        # Create a polynomial with these monomials
        polynomial = Polynomial(mono1, mono2)

        # Simplify the polynomial
        polynomial.simplify()

        # Ensure that the polynomial becomes zero and the head becomes None
        self.assertEqual(str(polynomial), "Polynomial: 0")
        self.assertIsNone(polynomial.head)

    def test_polynomial_equality(self):
        # Create monomials for polynomials
        mono1 = Mono(3, 2)
        mono2 = Mono(2, 1)
        mono3 = Mono(1, 0)

        # Create polynomials for comparison
        polynomial1 = Polynomial(mono1, mono2, mono3)
        polynomial2 = Polynomial(mono1, mono2)
        polynomial3 = Polynomial(mono1, Mono(3, 1), mono3)

        # Test equality
        self.assertTrue(polynomial1 == polynomial1)
        self.assertTrue(polynomial1 != polynomial2)
        self.assertFalse(polynomial1 == polynomial2)
        self.assertFalse(polynomial1 == polynomial3)

    def test_polynomial_equality_with_non_polynomial(self):
        # Create a polynomial
        mono1 = Mono(3, 2)
        mono2 = Mono(2, 1)
        polynomial = Polynomial(mono1, mono2)

        # Try to compare with a non-polynomial object

        non_polynomial = "This is not a polynomial"

        # Ensure that the comparison returns False
        self.assertFalse(polynomial == non_polynomial)

    def test_derivative_with_first_degree_one_monomials(self):
        # Create monomials for polynomials
        mono1 = Mono(2, 1)
        mono2 = Mono(3, 2)
        mono3 = Mono(4, 1)
        mono4 = Mono(5, 3)

        # Create a polynomial with these monomials
        polynomial = Polynomial(mono1, mono2, mono3, mono4)

        # Compute the derivative
        derivative = polynomial.derivative

        # Ensure that the first monomials with degree 1 are simplified after derivative
        self.assertEqual(str(derivative), "Polynomial: 6x+4+15x**2")

    def test_polynomial_multiplication_with_integer(self):
        # Create monomials for the polynomial
        mono1 = Mono(2, 1)
        mono2 = Mono(3, 2)

        # Create a polynomial with these monomials
        polynomial = Polynomial(mono1, mono2)

        # Multiply the polynomial by an integer
        multiplied_polynomial = polynomial * 3

        # Ensure that the multiplication is correct
        self.assertEqual(str(multiplied_polynomial), "Polynomial: 6x+9x**2")

    def test_polynomial_rmultiplication_with_integer(self):
        # Create monomials for the polynomial
        mono1 = Mono(2, 1)
        mono2 = Mono(3, 2)

        # Create a polynomial with these monomials
        polynomial = Polynomial(mono1, mono2)

        # Multiply an integer by the polynomial using __rmul__
        multiplied_polynomial = 3 * polynomial

        # Ensure that the multiplication is correct
        self.assertEqual(str(multiplied_polynomial), "Polynomial: 6x+9x**2")

    def test_copy_empty_polynomial(self):
        # Create a polynomial with non-empty monomials
        mono1 = Mono(2, 1)
        mono2 = Mono(3, 2)
        polynomial = Polynomial(mono1, mono2)

        # Set the head of the polynomial to None to simulate an empty polynomial
        polynomial.head = None

        # Copy the polynomial
        copied_polynomial = polynomial.copy()

        # Ensure that the copied polynomial also has an empty head
        self.assertEqual(str(copied_polynomial), "Polynomial: 0")

        self.assertIsNotNone(copied_polynomial.head)


if __name__ == "__main__":
    unittest.main()
