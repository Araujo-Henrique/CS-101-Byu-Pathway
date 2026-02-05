min_expectancy = 9999
max_expectancy = -1
respective_coutry_max = ""
respective_coutry_min = ""
respective_code_max = ""
respective_code_min = ""
respective_year_max = 1
respective_year_min = 9999
year_data = {}
count_data = {}

with open("life-expectancy.csv") as datas: # Accessing the file
    next(datas) # ignore the first line

    for line in datas: # This first line of code define just the lower and higher expectancy
        clean_line = line.strip() # Deleting each blank space
        parts = clean_line.split(",") # Creating a list according with each data in the file like "country, age, year".

        country = parts[0] # Coutries are in the first position
        code = parts[1]
        year = int(parts[2])
        expectancy = float(parts[3])
        
        if expectancy > max_expectancy: # Searching for the max life expectancy
            max_expectancy = expectancy # I can't just print the varuable expectancy[0]. I need to add it in another variable
            respective_coutry_max = country
            respective_year_max = year

        
        if expectancy < min_expectancy:
            min_expectancy = expectancy # I can't just print the varuable expectancy[0]. I need to add it in another variable
            respective_coutry_min = country
            respective_code_min = code
            respective_year_min = year

        if year in year_data:
            year_data[year] += expectancy
            count_data[year] += 1
        else:
            year_data[year] = expectancy
            count_data[year] = 1

    while True:
        try:
            user_choice = int(input("Please enter the year of interest: "))
            while user_choice < respective_year_min or user_choice > respective_year_max:
                print(f"Sorry. Our datas is just between the follow years: {respective_year_min}-{respective_year_max}")
                user_choice = int(input("Please enter the year of interest: "))
                if user_choice in (respective_year_min, respective_code_max):
                    break
                
        except ValueError:
            print("Please enter just the number.")
            continue
        else:
            break




# Verify the choosed year and the respective datas from him
    print(f"\nFor the year {user_choice}:")
    if user_choice in year_data:
        total_expectancy = year_data[user_choice]
        count = count_data[user_choice]
        average = total_expectancy / count

        print(f"{average:.2f}")