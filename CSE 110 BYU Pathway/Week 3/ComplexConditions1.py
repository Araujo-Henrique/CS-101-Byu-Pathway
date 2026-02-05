# A student makes honour roll if their arerage is >=.85
# and their lowest grade is not below 70

gpa = float(input("What was your Grade Point Average? "))
lowest_grade = float(input("What was your lowest grade? "))

if gpa >= .85 and lowest_grade >= .70: #To attend the honor the student need to attend both conditions
    print("You made the honour roll")