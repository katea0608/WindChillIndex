#Kate Anderson U21933376
#Abhinav Ravipati U19635451
#Driver: Kate
#Navigator: Abhinav


#Wind-Chill Temperature
#This program takes in a temp and wind speed and then calculates a wind chill index using the national weather service formula

import math #imports the math module
temperature = float(input("Enter the temperature in Fahrenheit: "))

while temperature < -58 or temperature > 41: #while loop only executes if one of the two statements is true
    print("Temperature must be between -58F and 41F")
    temperature = float(input("Please re-enter the temperature in Fahrenheit: "))

windspeed = float(input("Enter the wind speed milers per hour: "))

while windspeed < 2: #while loop executes while speed is less than 2
    print("Speed must be greater than or equal to 2")
    windspeed = float(input("Please re-enter the wind speed in miles per hour: "))
    
#wind chill equation using math module    
windchill_index = 35.74 + (0.6215 * temperature) - (35.75 *math.pow(windspeed, 0.16)) + (0.4275 * temperature * math.pow(windspeed, 0.16))

print("The wind chill index is","{:.3f}".format( windchill_index)) #prints the windchill index after while loops are done executing
#used formatting to get 3 decimal places
