
def equilateral(sides):
    """Determine if a triangle is equilateral (all sides equal).
    
    :param sides: list - three side lengths of a triangle
    :return: bool - True if equilateral, False otherwise
    """
    a, b, c = sides
    # All sides must be equal and greater than 0
    return a == b == c and a > 0


def isosceles(sides):
    """Determine if a triangle is isosceles (at least two sides equal).
    
    :param sides: list - three side lengths of a triangle
    :return: bool - True if isosceles, False otherwise
    """
    a, b, c = sides
    # Triangle inequality must hold and at least two sides equal
    return (a == b or b == c or a == c) and (a + b > c) and (a + c > b) and (b + c > a) and a > 0


def scalene(sides):
    """Determine if a triangle is scalene (all sides different lengths).
    
    :param sides: list - three side lengths of a triangle
    :return: bool - True if scalene, False otherwise
    """
    a, b, c = sides
    # All sides must be different and satisfy triangle inequality
    return (a != b and b != c and a != c) and (a + b > c) and (a + c > b) and (b + c > a) and a > 0
