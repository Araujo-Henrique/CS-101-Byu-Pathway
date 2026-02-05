# A student makes honour roll if their arerage is >=.85
# and their lowest grade is not below 70

gpa = float(input("What was your Grade Point Average? "))
lowest_grade = float(input("What was your lowest grade? "))

if gpa >= .85 and lowest_grade >= .70: #To attend the honor the student need to attend both conditions
    honour_rool = True # I creat a boolean variable
else:
    honour_roll = False # Now the variable can attend the boolean or not

"""Somewhere later in your code if you need to check if students is on honour roll,
all I need to do is check the boolean variable I ser earlier in my code"""
if honour_roll:
     print("You made the honour roll")
else:
     print("You didn't made honour roll")

     #Você pode combinar as funções com AND e também com OR