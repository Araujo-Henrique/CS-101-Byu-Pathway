
for i in range(5): # The code will print: 0-4
    print(i)
    for j in range(10, 13): # In each number the first code print, the sistem automatically will put the number 10-12
        print(f"--{j}")

        """ Hint: While we generally prefer variable names that are more descriptive than a single letter,
        if the variable will only be used for counting in a simple loop it is considered standard to use i.
        Then, if you have an inner loop, you use j, and a third inner loop would be k.
        If you have more than three loops you should consider if there is a simpler way to accomplish your task, and if there really isn't,
        you should at least move to more descriptive variable names at that point.""" 