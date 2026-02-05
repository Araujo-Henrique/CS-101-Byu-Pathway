#Calculating the price
child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))

#Calculating the number of children and adults and than multiplying by the price
children = int(input("How many children are there?  "))
adults = int(input("How many adults are there?  "))
subtotal = (child_meal * children) + (adult_meal * adults)
print(f"Subtotal: ${subtotal:.2f}")

#Calculating the sales tax
sales_tax_rate = float(input("What is the percentage of sales tax rate? "))
while sales_tax_rate < 1 :
   print("The Sales tax rate needs to be equal 1 or more.")
   sales_tax_rate = float(input("What is the percentage of sales tax rate? "))
sales_tax = subtotal * (sales_tax_rate / 100)
print(f"Sales Tax: ${sales_tax:.2f}")

total = subtotal + sales_tax
print(f"Total: ${total:.2f}")


#Calculating the payment
payment = float(input("What is the payment amount? "))   

while payment < total :
   print("You need to pay the total or more an than recive your change.")
   payment = float(input("What is the payment amount? "))   


#Giving the change
print("Thanks for buy")
   
change = payment - total

print(f"Change: ${change:.2f}")