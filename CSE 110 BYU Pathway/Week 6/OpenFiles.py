colors = open("colors.txt") # Essa variável se torna uma lista no momento em que abre o documento

for line in colors:
    print(line)

colors.close() # By this method you always need to close this file


with open("colors.txt") as colors: # This is other way to acess a file without need to close it
    for line in colors:
        print(line)

print("The file is closed now")