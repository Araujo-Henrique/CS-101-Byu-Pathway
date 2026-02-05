min_expectancy = 9999
max_expectancy = -1
respective_coutry_max = ""
respective_coutry_min = ""
respective_code_max = ""
respective_code_min = ""
respective_year_max = 1
respective_year_min = 9999
year_data = {} # Creating a directory to sum the years expectancies
count_data = {} # How many values per year?
country_min_expectancy = {} # This is find the years for the countries with less expectancies
country_max_expectancy = {} # This is find the years for the countries with more expectancies

with open("life-expectancy.csv") as datas: # Accessing the file
    next(datas) # Ignore the first line of the doccument (usally, the head who describing the datas)

    for line in datas: # This first line of code define just the lower and higher expectancy
        clean_line = line.strip() # Deleting each blank space
        parts = clean_line.split(",") # Creating a list according with each data in the file like "country, age, year".

        country = parts[0] # Coutries are in the first position
        code = parts[1]
        year = int(parts[2])
        expectancy = float(parts[3])
        
        # Searching for the max life expectancy
        if expectancy > max_expectancy: 
            max_expectancy = expectancy # I can't just print the varuable expectancy[0]. I need to add it in another variable
            respective_coutry_max = country
            respective_year_max = year

        
        if expectancy < min_expectancy:
            min_expectancy = expectancy 
            respective_coutry_min = country
            respective_code_min = code
            respective_year_min = year

        # Att the year_data according with the sum of the expectancies
        if year in year_data: 
            year_data[year] += expectancy
            count_data[year] += 1
        else:
            year_data[year] = expectancy
            count_data[year] = 1
        
        # Att the country diccionary according with the expectancy
        if year not in country_max_expectancy or expectancy > country_max_expectancy[year][1]:
            country_max_expectancy[year] = (country, expectancy)
        elif year  not in country_min_expectancy or expectancy < country_min_expectancy[year][1]:
            country_min_expectancy[year] = (country, expectancy)



    # Asking for user to choose some year and take care to the program don't crash
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


    # Output of the code
    print(f"\nThe overall max life expectancy is: {max_expectancy} from {respective_coutry_max} in {respective_year_max}")
    print(f"The overall min life expectancy is: {min_expectancy} from {respective_coutry_min} in {respective_year_min}")

    print(f"\nFor the year {user_choice}:")

    # Caulculating the datas before the last output
    if user_choice in year_data:
        total_expectancy = year_data[user_choice]
        count = count_data[user_choice]
        average = total_expectancy / count
        country_max_expectancy, max_expectancy = country_max_expectancy[user_choice]
        country_min_expectancy, min_expectancy = country_min_expectancy[user_choice]

        print(f"The average life expectancy across all countries was {average:.2f}")
        print(f"The max life expectancy was in {country_max_expectancy} with {max_expectancy:.2f}")
        print(f"The min life expectancy was in {country_min_expectancy} with {min_expectancy:.2f}")