'''
Chris Oakley
Arrays and Matrices
10/3/2020
EGN3214 - Assignment 7

Variables:

ureg = UnitRegistry for Pint

'''
from pint import UnitRegistry
ureg = UnitRegistry()
from scipy.constants import convert_temperature

temp = str(input('Enter Temperature with a space and the unit i.e. (C,F,K): ').upper())

pressure = str(input('Enter Pressure with a space and the unit i.e. (ATM, inHG, PSI): ').upper())



def get_temp(temp):
    # Convert F to Kelvin
    if temp[-1] == 'F':
        temp = int(temp[:-1])
        T = convert_temperature(temp, 'Fahrenheit', 'Kelvin')
        print(T)

    # Convert C to Kelvin
    elif temp[-1] == 'C':
        temp = int(temp[:-1])
        T = convert_temperature(temp, 'Celsius', 'Kelvin')
        print(T)

    # It is Kelvin
    elif (temp[-1] == 'K' or len(temp.split(' ')) == 1):
        if len(temp.split(' ')) == 1:
            T = int(temp)
            print(T)
        else:
            T = int(temp[:-1])
            print(T)
    # It is not Kelvin
    else:
        print('Please enter a valid temperature and unit!') 

    return T

def get_pressure():
    if pressure.split()[1] == 'PSI':
        pressure = int(pressure[:-3])
        P = pressure * ureg.psi
        print(P.to(ureg.atm))

    # Convert C to Kelvin
    elif pressure.split()[1] == 'INHG':
        pressure = int(pressure[:-4])
        P = pressure * ureg.inHg
        print(P.to(ureg.atm))


    # It is Kelvin
    elif pressure.split()[1] == 'ATM':
        pressure = int(pressure[:-3])
        P = pressure * ureg.atm
        print(P.to(ureg.atm))
    # It is not Kelvin
    else:
        print('Please enter a valid temperature and unit!') 

    return P