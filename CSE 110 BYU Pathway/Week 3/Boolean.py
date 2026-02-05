# Tip: Common boolean variable names are is_xxx, has_xxx, can_xxx, etc.

is_hot = True

# Using the "not" keyword
if not is_hot: #"convert" the boolean to  false
    print("It is not hot")

# It works, but is generally avoided to check if it is false:
if is_hot == False:
    print("It is not hot")