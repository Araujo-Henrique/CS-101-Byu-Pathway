import random

magic_number = random.randint(1,100) # Creating a random number

print("Hello! In this game, you need to guess the magic number")
print("During the game you will recive some hints in the number is lower or less than your guess")
print("Good luck for you!!")

print()


while True: # The values coudn't be a STR
    try:

        guess = int(input("What is the Magic Number? "))
        
        if guess <1 or guess >100:
            print("Hint: The Magic Number is between 1-100")

        while guess < magic_number: 
            print("Higher")
            guess = int(input("What is the Magic Number? "))
            if guess <1:
                print("Hint: The Magic Number is between 1-100") 
  
            
        while guess > magic_number:
            print("Lower")
            guess = int(input("What is the Magic Number? "))
            if guess > 100:
                print("Hint: The Magic Number is between 1-100")
  
            
    except ValueError: # The program avoid errors in this input.
        # If an error occours the program return to line 14
        print("Hint: The Magic Number is between 1-100")
        continue # If True, the loop ends

    else:
        break


print("Well done! You guessed it!")





