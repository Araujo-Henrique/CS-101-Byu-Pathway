length_num = 50
width_num = 10

# If you add the numbers together, you would get the result you expect:
print(length_num + width_num) # This displays: 60

# You can convert the values to the strings "50" and "10" like this:
length_string = str(length_num)
width_string = str(width_num)

# The computer now thinks of these variable as two characters, the digit 5 followed
# by the digit 0, and the digit 1 followed by the digit 0.

# If you try to add the two strings together, it will concatenate them, or display
# one after the other:
print(length_string + width_string) # This displays: 5010

#Another point is: INT values doesn't appear in a print with STR. you need to convert the INT value in a STR value first