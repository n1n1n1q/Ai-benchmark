"""
lab4.2
"""
def four_lines_area(koef1: float, const1: float, koef2: float, const2: float,
                      koef3: float, const3: float, koef4: float, const4: float)-> float:
    """
    Find and return the area of a convex quadrangle
    >>> four_lines_area(1,2,1,3,1,4,1,5)
    0
    >>> four_lines_area(0,-2,-2,3,3,4,1,5)
    30.86
    """
    try:
        px1,py1=lines_intersection(koef1, const1, koef2, const2)
        px2,py2=lines_intersection(koef2, const2, koef3, const3)
        px3,py3=lines_intersection(koef3, const3, koef4, const4)
        px4,py4=lines_intersection(koef4, const4, koef1, const1)
        side1=distance(px1,py1,px2,py2)
        side2=distance(px2,py2,px3,py3)
        side3=distance(px3,py3,px4,py4)
        side4=distance(px4,py4,px1,py1)
        diag1=distance(px1,py1,px3,py3)
        diag2=distance(px2,py2,px4,py4)
        if quadrangle_area(side1,side2,side3,side4,diag1,diag2) is None:
            return 0
        return quadrangle_area(side1,side2,side3,side4,diag1,diag2)
    except TypeError:
        return 0

def lines_intersection(koef1:float, const1:float, koef2:float, const2:float)->float and float:
    """
    Find and return the point of intersection of two lines
    If lines are parallel, return None
    >>> lines_intersection(1,-2,5,-1)
    (-0.25, -2.25)
    >>> lines_intersection(0,1,0,1)

    """
    if koef1 == koef2:
        return None
    x_intersec=(const2-const1)/(koef1-koef2)
    y_intersec=koef1*x_intersec+const1
    return round(x_intersec,2),round(y_intersec,2)


def distance(px1: float, py1: float, px2: float, py2: float)-> float:
    """
    Find and return distance between 2 points
    >>> distance(0,0,3,4)
    5.0
    >>> distance(1,4,-5,7)
    6.71
    """
    try:
        if px1 is None or px2 is None:
            return None
        dist=((px1-px2)**2+(py1-py2)**2)**0.5
        return round(dist,2)
    except TypeError:
        return None



def quadrangle_area(side_a: float, side_b: float, side_c: float,
                     side_d: float, diag_f1: float, diag_f2: float)-> float:
    """
    Find and return quadrangle's area. If the quadrangle doesn't exist, return None
    >>> quadrangle_area(3,4,3,4,5,5)
    12.0
    >>> quadrangle_area(10,11,1,2,1,1)

    """
    try:
        if side_a <=0 or side_b <=0 or side_c <=0 or side_d <=0:
            return None
        if diag_f1<=0 or diag_f2<=0:
            return None
        quad_square1=4*(diag_f1**2)*(diag_f2**2)
        quad_square2=(side_b**2+side_d**2-side_a**2-side_c**2)**2
        quad_square=((quad_square1-quad_square2)/16)**0.5
        if quad_square1<=quad_square2:
            return None
        return round(quad_square,2)
    except TypeError:
        return None
if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
