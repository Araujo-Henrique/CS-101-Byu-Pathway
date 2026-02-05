first_number = input("Please add a number: ") #doing inputs you will have a string by default
second_number = input("Please add a number: ")

print(first_number + second_number) #by this way the program will read like a string and will print with any math calculations

print(int(first_number) + int(second_number)) #by this way the program will read like a number and will print like a math calculation7
 
 #obs: convert INT or FLOAT values in STR values is necessarie when we get an input variable

 #unless...

#if you want to get an INT value on the input, you need to do the following example:
people_number = int(input("How many people are in the room? "))

print(people_number)