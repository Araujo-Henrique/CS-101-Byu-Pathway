with open("courses.txt") as courses_files:
    for line in courses_files:
        parts = line.split(",")
        # Now we have the courses in the left and the grade in the right, before the ","
        # It works like a list, so all courses will the in the "0" position and the grades in the "1" position
        name = parts[0]
        grade = float(parts[1]) # I want a float value to this

        print(f"{name} - {grade}")

