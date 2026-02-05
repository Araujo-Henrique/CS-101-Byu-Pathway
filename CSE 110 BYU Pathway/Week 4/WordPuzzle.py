# Program: Word Game
# Author: Henrique Almeida Araujo
# Course: CS110

import random

keep_playing = "yes" # In the final, if the user wants to play again, the game will restart.

while keep_playing == "yes":

    random_words = (["blessed", "games", "study", "pathway", "work", "bed", "grow", "sunday", "partner", "with"])

    secret_word = random.choice(random_words) # FOr each new game, the word can change, this make the game more funny.



    number_of_secret_letters = len(secret_word) # The program will count how manny letters our secret word have.


    guess_count = 0 # This is to calculate how many guess the user did.


    print("Welcome to the word guessing game! ")
    print("How to play: The sistem create a secret word and you need to guess it")
    print()
    print("While you try to guess, the game will help you or not, according with your guess")
    print("If some letter of the guess is in the right place it will appear in uppercase, but if the word have that letter but not in that position, the letter will appear in lowercase.")
    print("Have fun!")
    print()

    print("Your hint is:", end="") # How many letters have our word? This is a hint.
    for letter in secret_word: # Letter is a new variable that will traverse our secret word.
        print( "_", end="") # Ratter than print the word, the program um print "_" according the letters in our secret word

    print()

    guess = input("What is your guess? ") # An input for the user guess
    number_of_guess_letters = len(guess) # The program will count how manny letters the guess word have
    guess_count += 1


    while guess.lower() != secret_word.lower(): # While the answer doesn't match, the loop will continue
        while number_of_guess_letters != number_of_secret_letters: # This block is just to gave to user a hint that the guess need to have the same quantity of letters that the secret word
            print("Sorry, the guess must have the same number of letters as the secret word.")
            print(f"Your guess need to have {number_of_secret_letters} letters")
            guess = input("What is your guess? ") # An input for the user try some guess
            number_of_guess_letters = len(guess)
            guess_count += 1

        while number_of_guess_letters == number_of_secret_letters:
            for i in range(number_of_guess_letters):
                letter = guess.lower()[i] # the variable "i" will traverse the guess and return the hints according with each letter right.
                if letter == secret_word[i]: # If the letter is in the rigth place it will appear in uppercase.
                    print(letter.upper(), end="")
                elif letter in secret_word: # If the letter is right, but is in the wrong place, it will appear in lowercase.
                    print(letter.lower(), end="")
                else: # If the letter guessed don't match with the secret word, it continues appearing like "_".
                    print("_", end="")
            if guess.lower() == secret_word: # If guessed, the loop ends.
                 print()
                 break
            
            print()
    
            guess = input("What is your guess? ") # Later revice some hints according with the guess, the loop restart.
            guess_count += 1
     

    print("Good job! You guesed it!")
    print(f"It took you {guess_count} guesses")

    keep_playing = input("Would you like to play again (yes/no)? ") # If the user wish to play again, the game restart.
    if keep_playing.lower() == "yes": # The progam could read the word regardless of how it is written.
        keep_playing = True
    elif keep_playing.lower() == "no": # The progam could read the word regardless of how it is written.
        keep_playing = True
    else:
        keep_playing = False # If the anwer isn't "yes" or "not", the program don't stop, but ask the question again

    while keep_playing == False: # If the user wrote something wrong the program will repeat the answer.
        print("Sorry, this answer is invalid.")
        keep_playing = input("Would you like to play again (yes/no)? ")
        if keep_playing.lower == "no":
            break

print("Thaks for playing!")