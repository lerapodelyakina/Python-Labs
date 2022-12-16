import math
pi = math.pi

default_radius = 5 

def circle_perimeter(r = default_radius):
    per = 2*pi*r
    return per

def circle_area(r = default_radius):
    area = pi*(r**2)
    return area 