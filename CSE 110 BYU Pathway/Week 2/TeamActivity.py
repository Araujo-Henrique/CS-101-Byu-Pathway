import math

side_square = float(input("What is the length of a side of the square (cm)? "))
square_area = side_square ** 2

print(f"The area of the square in centimeters is: {square_area:.1f}")

square_meter = square_area / 100

print(f"The area of the square in meters is:{square_meter:.1f} cm\u00b2")

rectangle_length = float(input("What is the length of rectangle? "))
rectangle_width = float(input("What is the width of the rectangle? "))
rectangle_area = rectangle_length * rectangle_width

print(f"The area of the rectangle is: {rectangle_area:.1f}")

circle_radius = float(input("What is the radius of the circle? "))
pi = math.pi

circle_area = pi * (circle_radius**2)

print(f"The area of the circle is: {circle_area:.4f}")

length_value = float(input("Please enter a number: "))
area_of_square = length_value**2
print(f"The area of this length is {area_of_square:.2f}")
circle = pi * (length_value**2)
print(f"The radius of this length is {circle:.2f}")
volumes = circle ** 3
print(f"The volume of this length is {volumes:.2f}")
sphere = (4/3)  * pi * volumes
print(f"The sphere of this length is {sphere:.2f}")

