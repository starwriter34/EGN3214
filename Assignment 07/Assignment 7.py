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

v = 1.0 * ureg.atm
t = 1.0 * ureg.degree_Fahrenheit


print(v.dimensionality)
print(v)
print(v.to(ureg.pascal))
print(v.to(ureg.psi))
print(v.to(ureg.inch_Hg))
print(t)
print(t.to(ureg.kelvin))
print(t.to(ureg.degree_Celsius))