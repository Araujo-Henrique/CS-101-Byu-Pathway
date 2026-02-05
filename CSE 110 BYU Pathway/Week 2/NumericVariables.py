#To print a Variable number plus a Variable String we have 2 options:

number = 7
second_number = 3


print("The number is " + str(number) + ".") #First example: we converted the variable in a string

print(f"The number is {number}.") #Second example: the idea is the same, but we did it with a function in the print statement

#You can save the new result of the concatenation of strings:

soma = number + second_number

print(soma)