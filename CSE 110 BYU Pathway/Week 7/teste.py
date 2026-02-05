v = 0 # Wind speed in miles per hour



def windchill_calc(temperature, v):
    wind_speed = v ** 0.16
    #Windchill calc according the U.S. National Weather Service
    #Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V**0.16)
    return 35.74 + 0.6215 * temperature - 35.75 * wind_speed + 0.4275*temperature * wind_speed
    
temperature = float(input("What is the temperature? ")) # User choose the temperature

measurement_unit = input("Do you want to see the result in Fahrenheit or Celsius (F/C)? ")
measurement_unit.lower

def fahrenheit (v): # The function will run according the variable "v"
     for i in range(15):
        if v < 60:
            v += 5
            print(f"At temperature {temperature}F, and wind speed {v} mph, the windchill is: {windchill_calc(temperature, v):.2f}F")

def celsius (v):
    for i in range(15):
        if v < 60:
            v += 5
            print(f"At temperature {temperature}C, and wind speed {v} mph, the windchill is: {windchill_calc(temperature, v):.2f}C")

if measurement_unit == "f":
    fahrenheit(v)
    
elif measurement_unit == "c":
       celsius(v)









#windchill = windchill_calc(temperature, v)

#print(windchill)











