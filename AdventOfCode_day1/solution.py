import math
from os import getcwd
#get the current working directory
print(getcwd())

#calculating fuel required for modules
f = open("inputFile.txt", "r")
fuel =0
for moduleMass in f:
    fuel += math.floor(int(moduleMass)/3) -2

print("Fuel required for modules is " + str(fuel))

totalFuel = 0
f = open("inputFile.txt", "r")
for moduleMass in f:
    #fuel for each module
    currentFuel = math.floor(int(moduleMass)/3) -2
    totalFuel += currentFuel
    extraFuel = 0
    #fuel for each modules's fuel
    while currentFuel >=0:
        currentFuel = math.floor(currentFuel/3) -2
        if currentFuel >=0:
            extraFuel += currentFuel
    #total fuel
    totalFuel += extraFuel

print("Total fuel " + str(totalFuel))

