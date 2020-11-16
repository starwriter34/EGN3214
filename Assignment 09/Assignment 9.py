
'''
Chris Oakley
Functions Part 1
09/13/2020
EGN3214 - Assignment 4

Variables:

a,b,c - The sides of the triangle
numbreak - The max number the your looking for squared

The end result should equal out to 31875000 as the number we are looking for.

'''
import math

numbreak = 1000

break_for = False

for a in range(1,numbreak):
    for b in range(a+1,numbreak):
        c = numbreak-a-b
       
        if (a**2+b**2)==c**2:
            print(f' a: {a} b: {b} c: {c}')
            print(a*b*c)
            break_for = True
    if break_for == True:
        break
