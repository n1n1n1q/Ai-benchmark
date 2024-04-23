"""Line and Point"""
from typing import Self


class Point:
    """Point object"""

    def __init__(self, x: float, y: float) -> None:
        """Initialize point"""
        self.x = x
        self.y = y

    def __eq__(self, other: Self) -> bool:
        """compare two Points"""
        return self.x == other.x and self.y == other.y

class Line:
    """Line object"""

    def __init__(self, p1: Point, p2: Point) -> None:
        """Initialize Line"""

        if p1 == p2:
            raise ValueError("Can't create the line from equal points")

        self.p1 = p1
        self.p2 = p2

    def get_coefficients(self):
        """
        Return coefficients of equation
        a*x+b*y+c 
        """
        dx = self.p2.x - self.p1.x
        dy = self.p2.y - self.p1.y

        c = self.p1.x * dy - self.p1.y * dx

        return (-dy, dx, c)

    def intersect(self, other: Self) -> Point | None:
        """
        Return intersection point of two lines
        or None if they doesn't intersect
        """
        if not isinstance(other, Line):
            return None

        a1, b1, c1 = self.get_coefficients()
        a2, b2, c2 = other.get_coefficients()

        if (a1, b1, c1) == (a2, b2, c2):
            return self

        slope_1 = a1 / b1 if b1 != 0 else 1j
        slope_2 = a2 / b2 if b2 != 0 else 1j

        if slope_1 == slope_2:
            return None

        x = (c2*b1 - c1*b2) / (a1*b2 - a2*b1)

        if b1 != 0:
            y = - ( (a1/b1)*x + c1/b1 )
        else:
            y = - ( (a2/b2)*x + c2/b2 )

        return Point(round(x,2), round(y, 2))
