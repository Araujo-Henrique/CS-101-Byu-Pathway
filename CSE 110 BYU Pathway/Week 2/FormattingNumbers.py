cars = 3
people = 8

people_per_car = people / cars

# The colon (:) after the variable name indicates that you are going to specify how to format it.
# The period (.) indicates that you are setting the precision or number of decimal places.
# The number (in this example 2) indicates that you would like that number of decimal places to be displayed
# The f indicates that you want fixed-point notation.


# Round to 1 decimal
print(f"There are {people_per_car:.1f} people in each car.")
# Output: There are 2.7 people in each car.

# Round to 2 decimals
print(f"There are {people_per_car:.2f} people in each car.")
# Output: There are 2.67 people in each car.

# Round to 3 decimals
print(f"There are {people_per_car:.3f} people in each car.")
# Output: There are 2.667 people in each car.