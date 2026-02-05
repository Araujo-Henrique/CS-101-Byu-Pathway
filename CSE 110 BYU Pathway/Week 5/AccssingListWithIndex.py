
the_list = ["Numero 1", "Numero 2", "Numero 3", "Numero 4", "Numero 5"]

first = the_list[0] # gets the first item
second = the_list[1] # gets the second item
third = the_list[2] # gets the third item

index = int(input("Which index would you like to get? "))
user_choice = the_list[index] # gets the item at the index the user typed
# With the square brackets [] the index can access a specific position

print(user_choice)
print()
print("-----------------------------------------------------")
# Removing itens from a list:

the_list.pop(3) # Removes the item at index 3

the_list.pop() # Removes the last item

for numeros in the_list:
    print(numeros)