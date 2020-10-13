'''
Chris Oakley
Functions Part 1
09/13/2020
EGN3214 - Assignment 4

Variables:

pressure - List of Pressures
volume - List of Calculated Volumes

P - Pressure in atm
n - Number of mols
T - Temperature in Kelvin
R - Universal Gas Constant on atm.L/(mol.K)
V - volume in liters
temp - throw away variable

'''
from scipy.constants import convert_temperature
import matplotlib.pyplot as plt
import re

pressure = [0.8, 0.9, 1.0, 1.1, 1.2]
volume = []
n = 1
T = 473

def CalculateVolume(P, n, T):

    R = 0.0821 # Universal Gas Constant on atm.L/(mol.K)
    V = (n*R*T)/P

    return V

def calculatePlot():

    for P in pressure:
        volume.append(CalculateVolume(P, n, T))

    plt.xlabel("Pressure (atm)")
    plt.ylabel("Volume (liters)")
    plt.title(f'Pressure and Volume at {T:.2f} degrees Kelvin.')
    plt.scatter(pressure, volume, color='red')
    plt.show()

temperature = str(input('Enter Temperate as Temperature and Unit, i.e. 40 C Units are C,F,K default K: ').upper())
# Convert F to Kelvin
if temperature[-1] == 'F':
    temp = int(temperature[:-1])
    T = convert_temperature(temp, 'Fahrenheit', 'Kelvin')
    calculatePlot()

# Convert C to Kelvin
elif temperature[-1] == 'C':
    temp = int(temperature[:-1])
    T = convert_temperature(temp, 'Celsius', 'Kelvin')
    calculatePlot()

# It is Kelvin
elif (temperature[-1] == 'K' or len(temperature.split(' ')) == 1):
    if len(temperature.split(' ')) == 1:
        T = int(temperature)
        calculatePlot()
    else:
        T = int(temperature[:-1])
        calculatePlot()
# It is not Kelvin
else:
    print('Please enter a valid temperature and unit!') 