# We have different forms to use the simble "#"

first_name = "Henrique"
last_name = "Araujo"

example1 = "Hello, " + first_name + " " + last_name
example2 = "Hello, {} {}" .format(first_name, last_name)
example3 = "Hello, {0} {1}" .format(first_name, last_name)
# Only available in Python 3
example4 = f"Hello, {first_name} {last_name}"
# "f" no exemplo 4 significa format

print(example1)
print(example2)
print(example3)
print(example4)