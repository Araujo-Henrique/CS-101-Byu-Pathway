word = "book"
number_of_letters = 4

for index in range(number_of_letters):
    letter = word[index] # If I didn't it and just use "print(index)" the program will show: 0, 1, 2 and 3 because the letters
    print(f"Index: {index} Letter: {letter}")


    """The previous example assumed the number of letters, or length of the string, would always be 4,
    but this will not work if the string has more or fewer letters. Instead of typing the 4 directly,
    you can let the computer find the length by using the len function.
    The following code shows how to use len to get the length of a string:"""

    print("------------------------------------------------------")


dog_name = input("What is your dog's name? ")
letter_count = len(dog_name)

print(f"Your dog's name has {letter_count} letters")

