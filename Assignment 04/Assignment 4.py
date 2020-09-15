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

'''
# import matplotlib.pyplot as plt
# import re

# pressure = [0.8, 0.9, 1.0, 1.1, 1.2]
# volume = []
# n = 1
# T = 473




# def CalculateVolume(P, n, T):

#     R = 0.0821 # Universal Gas Constant on atm.L/(mol.K)
#     V = (n*R*T)/P

#     return V
# for P in pressure:
#     volume.append(CalculateVolume(P, n, T))
# #print(f'The volume is {v:.2f} L')

# plt.xlabel("Pressure (atm)")
# plt.ylabel("Volume (liters)")
# plt.scatter(pressure, volume)
# plt.show()

temperature = str(input('Enter Temperate as Temperature and Unit, i.e. 40 C Units are C,F,K defualt K: ').upper())

print(temperature.split(' '))
print(len(temperature.split(' ')))

if temperature[-1] == 'F':
    print('Fahrenheit')
elif temperature[-1] == 'C':
    print('Celsius')
elif (temperature[-1] == 'K' or temperature[-1] == ' ' or len(temperature.split(' ')) ==  1):
    print('Kelvin')
else:
    print('Please enter a valid temperature and unit!') 
