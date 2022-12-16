import math
default_a = 7
default_b = 2
default_c = 8

def triangle_perimeter(a = default_a, b = default_b, c = default_c):
    perimeter = a + b + c
    return perimeter

def triangle_area(a = default_a, b = default_b, c = default_c):
    half = (a + b + c)//2
    area = math.sqrt(half*(half - a)*(half - b)*(half - c))
    return area
