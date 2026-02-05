
color = input("What is your favorite color? ")

# This if statement will only match "blue" not "Blue" or "BLUE"
if color == "blue":
    print("I like blue too.")

# This if statement will match the word blue, regardless of the capitalization
if color.lower() == "blue":
    print("I like blue too.")