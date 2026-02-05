province = input("What is your province? ")

if province.capitalize() == "Alberta" or province == "Nunavut" : #Se o input for um OU (or) outro a condição é a mesma
    tax = 0.05
elif province.capitalize() == "ONtario" : #Se não pode ser essa
    tax = 0.13
else: #Se não for nenhuma das outras esse vai ser a condição
    tax = 0.15