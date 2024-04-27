import unittest
from line_and_point import Point, Line
import random

class TestPoint(unittest.TestCase):
    def test_point_creation(self):
        point = Point(3, 4)
        self.assertEqual(point.x, 3)
        self.assertEqual(point.y, 4)

    def test_point_equality(self):
        point1 = Point(3, 4)
        point2 = Point(3, 4)
        point3 = Point(4, 5)
        self.assertEqual(point1, point2)
        self.assertNotEqual(point1, point3)

class TestLine(unittest.TestCase):
    def setUp(self):
        self.point1 = Point(1, 2)
        self.point2 = Point(3, 4)

    def test_line_creation(self):
        line = Line(self.point1, self.point2)
        self.assertEqual(line.p1, self.point1)
        self.assertEqual(line.p2, self.point2)

    def test_line_invalid_creation(self):
        with self.assertRaises(ValueError):
            Line(self.point1, self.point1)

    def test_get_coefficients(self):
        line = Line(self.point1, self.point2)
        coeffs = line.get_coefficients()
        self.assertEqual(coeffs, (-2, 2, -2))

    def test_intersect_parallel_lines(self):
        line1 = Line(Point(1, 1), Point(2, 2))
        line2 = Line(Point(2, 1), Point(3, 2))
        self.assertIsNone(line1.intersect(line2))

    def test_intersect_coinciding_lines(self):
        line1 = Line(Point(1, 1), Point(2, 2))
        line2 = Line(Point(1, 1), Point(2, 2))
        self.assertEqual(line1.intersect(line2), line1)

    def test_intersect_non_parallel_lines(self):
        line1 = Line(Point(0, 0), Point(3, 3))
        line2 = Line(Point(0, 2), Point(2, 0))
        intersection = line1.intersect(line2)
        self.assertEqual(intersection.x, 1)
        self.assertEqual(intersection.y, 1)

    def test_intersect_vertical_line(self):
        line1 = Line(Point(1, 1), Point(1, 5))
        line2 = Line(Point(2, 2), Point(2, 6))
        intersection = line1.intersect(line2)
        self.assertIsNone(intersection)

    def test_intersect_horizontal_line(self):
        line1 = Line(Point(1, 1), Point(5, 1))
        line2 = Line(Point(2, 2), Point(6, 2))
        intersection = line1.intersect(line2)
        self.assertIsNone(intersection)

    def test_intersect_identical_lines(self):
        line1 = Line(Point(1, 1), Point(3, 3))
        line2 = Line(Point(1, 1), Point(3, 3))
        self.assertEqual(line1.intersect(line2), line1)

    def test_intersect_lines_with_zero_slope(self):
        line1 = Line(Point(0, 0), Point(3, 0))
        line2 = Line(Point(1, 1), Point(1, 5))
        intersection = line1.intersect(line2)
        self.assertEqual(intersection.x, 1)
        self.assertEqual(intersection.y, 0)

    def test_intersect_lines_with_infinite_slope(self):
        line1 = Line(Point(1, 1), Point(1, 2))
        line2 = Line(Point(1, 2), Point(2, 2))
        intersection = line1.intersect(line2)
        self.assertEqual(intersection.x, 1)
        self.assertEqual(intersection.y, 2)

    def test_intersect_lines_with_zero_division(self):
        with self.assertRaises(ValueError):
            line1 = Line(Point(1, 1), Point(1, 1))
            line2 = Line(Point(2, 2), Point(2, 2))
            line1.intersect(line2)

    def test_boundary_points(self):
        # Test with points on the boundaries
        point_zero = Point(0, 0)
        point_max = Point(float('inf'), float('inf'))
        line1 = Line(point_zero, point_max)
        self.assertEqual(line1.get_coefficients(), (-float('inf'), float('inf'), 0))

    def test_randomized_intersection(self):
        # Test intersection with randomly generated lines
        for _ in range(100):
            x1, y1 = random.uniform(-100, 100), random.uniform(-100, 100)
            x2, y2 = random.uniform(-100, 100), random.uniform(-100, 100)
            x3, y3 = random.uniform(-100, 100), random.uniform(-100, 100)
            x4, y4 = random.uniform(-100, 100), random.uniform(-100, 100)
            line1 = Line(Point(x1, y1), Point(x2, y2))
            line2 = Line(Point(x3, y3), Point(x4, y4))
            intersection = line1.intersect(line2)
            # If the lines are parallel or coinciding, expect None, otherwise, expect a Point
            if line1.intersect(line2) is None:
                self.assertTrue(line1.get_coefficients() == line2.get_coefficients())
            else:
                self.assertTrue(isinstance(intersection, Point))

    def test_intersect_vertical_and_horizontal_lines(self):
        # Test intersection with vertical and horizontal lines
        vertical_line = Line(Point(1, 0), Point(1, 5))
        horizontal_line = Line(Point(0, 2), Point(5, 2))
        intersection = vertical_line.intersect(horizontal_line)
        self.assertEqual(intersection, Point(1, 2))

    def test_intersect_diagonal_lines(self):
        # Test intersection with diagonal lines
        diagonal_line1 = Line(Point(0, 0), Point(3, 3))
        diagonal_line2 = Line(Point(0, 3), Point(3, 0))
        intersection = diagonal_line1.intersect(diagonal_line2)
        self.assertEqual(intersection, Point(1.5, 1.5))

    def test_intersect_with_multiple_intersections(self):
        # Test intersection with multiple lines intersecting at various points
        line1 = Line(Point(0, 0), Point(4, 0))
        line2 = Line(Point(2, 2), Point(2, -2))
        line3 = Line(Point(1, 1), Point(3, 3))
        intersection = line1.intersect(line2)
        self.assertEqual(intersection, Point(2, 0))
        intersection = line1.intersect(line3)
        self.assertEqual(intersection, Point(0, 0))

    def test_intersect_with_line_segments(self):
        # Test intersection with line segments
        line1 = Line(Point(0, 0), Point(4, 0))
        line2 = Line(Point(2, 2), Point(2, -2))
        intersection = line1.intersect(line2)
        self.assertEqual(intersection, Point(2, 0))

    def test_intersect_with_single_point(self):
        # Test intersection with lines intersecting at a single point
        line1 = Line(Point(1, 1), Point(3, 3))
        line2 = Line(Point(1, 3), Point(3, 1))
        intersection = line1.intersect(line2)
        self.assertEqual(intersection, Point(2, 2))

    def test_intersect_with_collinear_lines(self):
        # Test intersection with collinear lines
        line1 = Line(Point(1, 1), Point(3, 3))
        line2 = Line(Point(0, 0), Point(2, 2))
        self.assertEqual(line1.intersect(line2), line1)

    def test_intersect_with_overlapping_lines(self):
        # Test intersection with overlapping lines
        line1 = Line(Point(0, 0), Point(4, 4))
        line2 = Line(Point(2, 2), Point(6, 6))
        intersection = line1.intersect(line2)
        self.assertEqual(intersection, line1)

    def test_intersect_with_non_line_type_returns_none(self):
        # Test intersection with non-Line type should return None
        line1 = Line(Point(1, 1), Point(3, 3))
        point = Point(2, 2)
        intersection = line1.intersect(point)
        self.assertIsNone(intersection)

if __name__ == '__main__':
    unittest.main()
