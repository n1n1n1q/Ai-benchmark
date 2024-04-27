import unittest
from line_and_point import Point, Line

class TestLine(unittest.TestCase):
    """Test cases for Line class"""

    def setUp(self):
        """Set up points and lines for testing"""
        self.points = {
            "point_1_1": Point(-4, 0),
            "point_1_2": Point(0, -4),
            "point_2_1": Point(-0.5, 0),
            "point_2_2": Point(0, -1),
            "point_3_1": Point(0, 0),
            "point_3_2": Point(0, 1),
            "point_4_1": Point(0, 0),
            "point_4_2": Point(1, 0),
            "point_5_1": Point(-5, 0),
            "point_5_2": Point(0, -5),
            "point_6_1": Point(-0.25, 0),
            "point_6_2": Point(0, 1),
            "point_7_1": Point(4, 0),
            "point_7_2": Point(0, 1),
            "point_8": Point(0, 2),
            "point_9": Point(1, 2),
            "point_10": Point(0, 3),
            "point_11": Point(1, 3),
            "point_12": Point(0, 1),
            "point_13": Point(1, 1),
            "point_14": Point(1, 2),
        }

        self.lines = {
            "line1": Line(self.points["point_1_1"], self.points["point_1_2"]),
            "line2": Line(self.points["point_2_1"], self.points["point_2_2"]),
            "line3": Line(self.points["point_5_1"], self.points["point_5_2"]),
            "line4": Line(self.points["point_6_2"], self.points["point_6_1"]),
            "line5": Line(self.points["point_7_2"], self.points["point_7_1"]),
            "line6": Line(self.points["point_8"], self.points["point_9"]),
            "line7": Line(self.points["point_10"], self.points["point_11"]),
            "line8": Line(self.points["point_12"], self.points["point_13"]),
            "line9": Line(self.points["point_13"], self.points["point_14"]),
            "line10": Line(self.points["point_13"], self.points["point_14"]),
            "vertical_line": Line(self.points["point_3_1"], self.points["point_3_2"]),
            "horizontal_line": Line(self.points["point_4_1"], self.points["point_4_2"]),
        }

    def test_point_init(self):
        """Test initialization of Point objects"""
        self.assertEqual(self.points["point_1_1"].x, -4)
        self.assertEqual(self.points["point_1_1"].y, 0)
        self.assertEqual(self.points["point_1_2"].x, 0)
        self.assertEqual(self.points["point_1_2"].y, -4)

    def test_line_init(self):
        """Test initialization of Line objects"""
        self.assertEqual(self.lines["line1"].p1, self.points["point_1_1"])
        self.assertEqual(self.lines["line1"].p2, self.points["point_1_2"])
        self.assertEqual(self.lines["line2"].p1, self.points["point_2_1"])
        self.assertEqual(self.lines["line2"].p2, self.points["point_2_2"])
        with self.assertRaises(ValueError):
            Line(self.points["point_1_1"], self.points["point_1_1"])

    def test_intersection_with_non_line(self):
        """Test intersection method with non-Line object"""
        self.assertIsNone(self.lines["line1"].intersect(1))

    def test_line_intersection(self):
        """Test intersection of two lines"""
        intersection_point = self.lines["line1"].intersect(self.lines["line2"])
        self.assertAlmostEqual(intersection_point.x, 3)
        self.assertAlmostEqual(intersection_point.y, -7)

    def test_backwards_line_intersection(self):
        """Test intersection of lines with points in inverse order"""
        intersection_point = self.lines["line4"].intersect(self.lines["line5"])
        self.assertEqual(intersection_point, Point(0, 1))

    def test_vertical_horizontal_line_intersection(self):
        """Test intersection of vertical and horizontal lines"""
        intersection_point = self.lines["vertical_line"].intersect(self.lines["horizontal_line"])
        self.assertEqual(intersection_point, Point(0, 0))

    def test_intersection_of_same_lines(self):
        """Test intersection of same lines"""
        intersection_point = self.lines["vertical_line"].intersect(self.lines["vertical_line"])
        self.assertEqual(intersection_point, self.lines["vertical_line"])
        self.assertEqual(self.lines["line9"].intersect(self.lines["line10"]), self.lines["line9"])

    def test_parallel_lines(self):
        """Test intersection of parallel lines"""
        intersection_point = self.lines["line1"].intersect(self.lines["line3"])
        self.assertIsNone(intersection_point)

    def test_two_horizontal_lines(self):
        """Test intersection of two parallel lines"""
        intersection_point = self.lines["line6"].intersect(self.lines["line7"])
        self.assertIsNone(intersection_point)


if __name__ == "__main__":
    unittest.main()
