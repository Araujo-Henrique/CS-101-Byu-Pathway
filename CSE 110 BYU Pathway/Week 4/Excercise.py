# Step 1: Make the Favorite Letter uppercase

word = "commitment"

favorite_letter = input("What is your favorite letter? ")


for letter in word : # Searching the favorite letter in the word
    # If foud the letter, that will appear in CAP
    if letter.lower() == favorite_letter.lower():
        print(letter.upper())
        # If not, the sistem will print the rest of the word
    else:
        print(letter.lower())

print()

print("----------------------------------------")
# Step 2: Clean up the Output

seccond_word = "powerfull"

seccond_favorite_letter = input("What is your seccond favorite letter? ")

for letter in seccond_word : 
    if letter.lower() == seccond_favorite_letter.lower():
        print(letter.upper(), end="") 
    else: # This is the same example, but because the function "end" the print will appear side by side
        print(letter.lower(), end="")

print()

print("----------------------------------------")

# Step 3: Hide the Letter

third_word = "Harry Potter"

third_favorite_letter = input("What is your third favorite letter? ")

for letter in third_word:
    if letter.lower() == third_favorite_letter.lower():
        letter = "_" # The origram will change the favorite letter to a "_"
        print(letter, end="")
    else:
        print(letter.lower(), end="")

