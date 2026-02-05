numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# It can be a large task if you need to work with many numbers
# Here is an easier way:


for number in numbers: #Example one
    print(number)

print("-------------------------------------------------")


numeros = range(21) # Example 2. Have 21 numbers here

for numero in range(11, 21): # I choose to print starting by the number 11 until the number 20 (the number 21 doesn't appear)
    print(numero)


# Hint: In programming languages we usually start counting at 0 instead of 1


print("-------------------------------------------------")

# This loop will start with 100, and go up to, but not including 200. Another point is that it will count by 10's
for i in range(100, 200, 10):
    print(i)