print("Welcome to Shopping Cart progam!")

itens = ["Add item", "View cart", "Remove item", "Compute total", "Quit"]
options = [1, 2, 3, 4, 5] # This is a specific list to walk with the itens list. 
cart = [""] # The first position start by 0. Now, the follow inputs will beggining at position 1
prices = [""] # The first position start by 0. Now, the follow inputs will beggining at position 1

user_select = "" # Creating a variable to use during the program for the user choice

while user_select != "quit":

    if user_select != "quit":

        print("\n Please select one of the following: ")
        for i in range(len(options)): # The variable i will walk into the list option loking foward positions. The value "int" in there will be count by position only
            item = itens[i] # This is to print the item in the list one by one
            option = options[i] # This is to print the item in the list one by one
            print(f"{option}. {item}")
        
    
    user_select = input("\n Please, enter an action tiping the number: ")

    if user_select == "1":
        new_product = input("What item would you like to add in the cart? ")
        cart.append(new_product) # Adding an item to the cart list starting by the position "1"
        while True:
            try:
                quantity = int(input("How many? "))
                value = float(input(f"What is the price of '{new_product}'? "))
                value = value*quantity # multiply the price acoording the quantity
            except ValueError: # If the user input an str for example, the program won't crash. Ratter than crash the program will do the following:
                print("Please enter just the number.")
                continue
            else:
                break 
        prices.append(value)
        print(f"The product '{new_product}' has been added to the cart.")

    elif user_select == "2":
        for i in range(1,len(cart)): # The list will jump the empty value and will start the cpunt by 1
            product = cart[i]
            price = prices[i]
            print(f"{i}. {product} - ${price}")

    elif user_select == "3":
        while True:
            try:
                index = int(input("Which item would you like to remove? Please enter the number "))
                cart.pop(index)
                prices.pop(index)
                print(f"The item was removed from the cart.")
                break
            except ValueError:
                print("Sorry, you need to enter just the number of the item.")
                continue


    elif user_select == "4":
        total = sum(prices)
        print(f"The total of your shop is ${total:.2f}.")

    elif user_select == "5":
        break
    else:
        print("Sorry, this option isn't right. Please try again.")

print("Thank you. See you latter.")