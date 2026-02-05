import math


def compute_area_square (side_square):
    return side_square ** 2




def compute_area_rectangle (rectangle_length, rectangle_width):
    return rectangle_length * rectangle_width
    


def compute_area_circle (circle_radius):
    pi = math.pi
    return pi * (circle_radius**2)


shape = ""
while shape != quit:
    shape = input("What is your kind of shape between square, rectangle or circle? ")

    shape.lower

    if shape == "square":
        side_square = float(input("What is the length of a side of the square? "))
        area = compute_area_square(side_square)
        print(f"The square area is {area}")

    elif shape == "rectangle":
        rectangle_length = float(input("What is the length of rectangle? "))
        rectangle_width = float(input("What is the width of the rectangle? "))
        area = compute_area_rectangle(rectangle_length, rectangle_width)
        print(f"The rectangle area is {area}")

    elif shape == "circle":
        circle_radius = float(input("What is the radius of the circle? "))
        area = compute_area_circle(circle_radius)
        print(f"The circle radius is {area}")