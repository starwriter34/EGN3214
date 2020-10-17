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
Q = ureg.Quantity

continue_yn='y'
question = 'ask'
volume = (
    ['500 C', '1 atm'],
    ['100 F', '30 inHg'],
    ['500 K', '5 psi'],
    )

def get_temp(temp):
    # Convert F to Kelvin
    if temp.split()[1] == 'F':
        temp = int(temp[:-2])
        T = Q(temp, ureg.degF)

    # Convert C to Kelvin
    elif temp.split()[1] == 'C':
        temp = int(temp[:-2])
        T = Q(temp,ureg.degree_Celsius)

    # It is Kelvin
    elif temp.split()[1] == 'K':
        temp = int(temp[:-2])
        T = Q(temp, ureg.kelvin)
    else:
        print('Please enter a valid temperature and unit!') 

    return T.to('kelvin')

def get_pressure(pressure):
    if pressure.split()[1] == 'PSI':
        pressure = int(pressure[:-3])
        P = pressure * ureg.psi

    # Convert C to Kelvin
    elif pressure.split()[1] == 'INHG':
        pressure = int(pressure[:-4])
        P = pressure * ureg.inHg

    # It is Kelvin
    elif pressure.split()[1] == 'ATM':
        pressure = int(pressure[:-3])
        P = pressure * ureg.atm
    # It is not Kelvin
    else:
        print('Please enter a valid temperature and unit!') 

    return P.to('atm')

def calculateVolume(P, T):
    n = 1 * ureg.mole
    R = Q(0.0821, 'L*atm/(mole*K)') # Universal Gas Constant on atm.L/(mol.K)
    V = (n*R*T)/P

    return V

while continue_yn=='y':

    if question == 'ask':
        question = str(input('Do you wish to (M)anually Calculate the Volume, or run the (A)ssignment Numbers (M or A)?').upper())
    
    elif question == 'M':
        temp = str(input('Enter Temperature with a space and the unit i.e. (C,F,K): ').upper())
        pressure = str(input('Enter Pressure with a space and the unit i.e. (ATM, inHG, PSI): ').upper())

        T = get_temp(temp)
        P = get_pressure(pressure)

        P.to('atm')
        T.to('kelvin')

        V = calculateVolume(P,T)
        print()
        print(f'The volume is: {V:.2f}')
        print()
        continue_yn = input('Do you wish to continue? (Y or N)').lower()

    elif question == 'A':
        for items in volume:
            
            T = get_temp(items[0].upper())
            P = get_pressure(items[1].upper())

            V = calculateVolume(P,T)
            
            print(f'The Pressure is: {P:.2f}')
            print(f'The Temperature is: {T:.2f}')
            print('#'*41)
            print(f'The volume is: {V:.2f}')
            print()
            print()

        question = 'ask'
    elif question == 'Q':
        break

    else:
        print('Not a valid choice, please choose M or A')
        question = 'ask'