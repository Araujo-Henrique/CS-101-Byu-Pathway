grade = int(input("What is the percentage of your grade? (please use just the number) "))

if grade >= 90 : 
    letter = "A" # Converting the grade to a new STR variable
    print(f"This is your grade: {letter}")
elif grade >= 80 :
    letter = "B" # Converting the grade to a new STR variable
    print(f"This is your grade: {letter}")
elif grade >= 70 :
    letter = "C" # Converting the grade to a new STR variable
    print(f"This is your grade: {letter}")
elif grade >= 60 :
    letter = "D" # Converting the grade to a new STR variable
    print(f"This is your grade: {letter}")
else :
    letter = "F" # Converting the grade to a new STR variable
    print(f"This is your grade: {letter}")

if letter in("A", "B", "C") : # This is the note that determine if the user passed the course
    grade = True # Boolean variable to calculate the grade

else : 
    grade = False # Boolean variable to calculate the grade

if grade : # Return the boolean
        print("Congratulations! You did it! Now you can start the next term.")
else : # Return the boolean
    print("Sorry, you don't reach the grade, but don't be afraid, a growth mindset also is the abilit to try again and we will stay with you to help!")