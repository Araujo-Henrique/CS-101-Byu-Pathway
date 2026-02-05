country = input("Were are you from? ")

if country.capitalize() == "Canada": #Mesmo que o input tenha sido minusculo ele vai identificar com somente a primeira maiúscula
    province = input("Witch province? ") #Esse if está dentro do primeiro, pois se o primeiro é atendido será necessário identificar a provincia depois
    if province.capitalize() in("Alberta", "Nunavut", "Yukon"):
        tax = 0.05
    elif province.capitalize == "Ontario":
        tax = 0.13
    else:
        tax = 0.15

else: #Se o primeiro if não for atendido o programa vem direto para cá. Por exemplo se o usuário colocar outro pais que não seja canada
    tax = 0.0