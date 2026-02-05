word = "book"
number_of_letters = len(word) # Notice this can now work for any string

for index in range(number_of_letters):
    letter = word[index]
    print(f"Index: {index} Letter: {letter}")


print("------------------------------------------------------")


"""Using a for loop and the length of the string is a standard way to access both the index and the letter.
    However, Python also has a way to access both of these variables directly
    using a special function called enumerate as shown in the following example:"""

    
first_name = "Brigham"

# Notice by using enumerate, we specify both i and letter
for i, letter in enumerate(first_name):
    print(f"The letter {letter} is at position {i}")