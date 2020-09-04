'''
Chris Oakley
Interpolation
08/31/2020
EGN3214 - Assignment 2

Variables:

xp = list of rain fall in hours
fp = list of rain fall in inches
i = throw away variable for hours
plural = logic for hours or hour depending on the amout of time entered
'''

import numpy as np

xp = [0, 1, 2, 5, 7, 8, 10, 12, 15]
fp = [0, 0.4, 0.6, 1.3, 2.1, 2.9, 3.4, 3.7, 3.9]

while True:
    question = input('Enter Time in hours (M)anually or use (A)ssignment Times (M or A)? ').upper()

    if question == 'A':

        for i in range(1,16):
            if i > 1:
                plural = 'hours'
            else:
                plural = 'hour'

            print(f'The rain fall for {i} {plural} is {np.interp(i, xp, fp):.2f} inches.')
        break
    
    if question == 'M':

        i = float(input('Enter Time in hours (number can be a float) '))
        
        if i > 1:
            plural = 'hours'
        else:
            plural = 'hour'

        print(f'The rain fall for {i} {plural} is {np.interp(i, xp, fp):.2f} inches.')
        break