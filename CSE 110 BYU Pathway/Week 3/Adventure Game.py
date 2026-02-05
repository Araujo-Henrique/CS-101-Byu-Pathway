# This is a game to choose some options during a day and than, see the result acoording your choices.

print("Welcome to the Game of Choices! Here you will learning how the daily choices are important.")
print("How to play? It's easy, you need to choose the words in CAPS during the game and see the result. Have fun :)")

day = input("Please select a day between WEEKDAY, SATURDAY or SUNDAY. ")

if day.capitalize() in("Weekday", "Saturday", "Sunday") : # The progam will read the answer and understand if is correct or wrong.
    choice = True # Correct answer.
else :
    choice = False #Wrong answer.

    while choice == False : # If the user choose something different the question will repeat.
        print("Please, select a valid answer.")
        day = input("Please select a day between WEEKDAY, SATURDAY or SUNDAY. ")
        if day.capitalize() in("Weekday", "Saturday", "Sunday") : # The progam will read the answer and understand if is correct or wrong.
            choice = True # Correct answer.

print("-------------------------------------------------------------------")

if day.capitalize() == "Weekday" : # Game for the option 1.
   option1 = input("It's 7 a.m in a Monday. You wake up and have 2 options: prepare to the WORK or REST a little more. What is your choice? ")
   if option1.capitalize() in("Work", "Rest") :
       choice1 = True
   else :
        choice1 = False

        while choice1 == False : # If the user choose something different the question will repeat.
            print("Please, select a valid answer.")
            option1 = input("It's 7 a.m in a Monday. You wake up and have 2 options: prepare to the WORK or REST a little more. What is your choice? ")
            if option1.capitalize() in("Work", "Rest") :
                choice1 = True
        

   if option1.capitalize() == "WORK" :
       print("You have a great day of work and your boss offer you a promotion. Congratulations!!")
   else :
       print("""Your lost the time and don't wake up to go to your work. Your boss call you and tell you that you lose an opportunity of promotion.
             A new opportunity will appear just in 1 year.""")



elif day.capitalize() == "Saturday" : # Game for the option 2.
    option2 = input("Good morning! It's Saturday. After a long week of work your friends invite you to play soccer. What you want, play FOOTBALL or pass a time with your FAMILY? ")
    if option2.capitalize() in("Football", "Family") :
        choice2 = True
    else :          
        choice2 = False

        while choice2 == False : # If the user choose something different the question will repeat.
            print("Please, select a valid answer.")
            option2 = input("Good morning! It's Saturday. After a long week of work your friends invite you to play soccer. What you want, play FOOTBALL or pass a time with your FAMILY? ")
            if option2.capitalize() in("Football", "Family") :
                choice2 = True

    if option2.capitalize() == "Football" :
        print("You could play a little with your friends but forgot about the music presentation of you childs. It was important to them.")
    else :
        print("You choose to pass a time with your family. This was a great choice. Your childs had a music presentation and you was there to look them and was maravelous!")
        




else : # Game for the option 3.
    option3 = input("Every Sunday it's a good day to learning in the church. Your car brooken and you need to walk 3 km to the church. You have 2 options: call to bishop and STAY in your house this Sunday or WALK to church. ")
    if option3.capitalize() in("Stay", "Walk") :
        choice3 = True
    else :          
        choice3 = False

        while choice3 == False : # If the user choose something different the question will repeat.
            print("Please, select a valid answer.")
            option3 = input("Every Sunday it's a good day to learning in the church. Your car brooken and you need to walk 3km to the church. You have 2 options: call to bishop and STAY in your house this Sunday or WALK to church. ")
            if option3.capitalize() in("Stay", "Walk") :
                choice3 = True

    if option3.capitalize() == "Stay" :
        print("God loves the effort. If you want to bless your life and your family, it's necessary do some sacrifices.")
    else :
        print("Walking to the church you found a friend who could help you and take you and your family with his car to the church. The sacramental was so spitirual.")



print("-------------------------------------------------------------------")
print("This is the end of our game. Remember that our choises can change our eternity")



        