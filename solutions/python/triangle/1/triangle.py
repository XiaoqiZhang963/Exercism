def equilateral(sides):
    """The function determines if the triangle is equilateral
    Parameters:
    sides - list of the 3 sides of the triangle
    
    Returns:
    Bool - whether the given sides make a equilateral triangle"""
    if not isinstance(sides, list):
        return False
    if len(sides)!=3:
        return False
    a, b, c = sides
    if a<=0 or b<=0 or c<=0:
        return False
    if a+b<=c or a+c<=b or b+c<=a:
        return False
    return a==b==c



def isosceles(sides):
    if not isinstance(sides, list):
        return False
    if len(sides)!=3:
        return False
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a<=0 or b<=0 or c<=0:
        return False
    if a+b<c or a+c<b or b+c<a:
        return False
    return a==b or a==c or b==c


def scalene(sides):
    if not isinstance(sides, list):
        return False
    if len(sides)!=3:
        return False
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a<=0 or b<=0 or c<=0:
        return False
    if a+b<c or a+c<b or b+c<a:
        return False
    return a!=b and b!=c and a!=c
