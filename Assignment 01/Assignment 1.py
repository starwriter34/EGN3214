'''
Chris Oakley
Distnace/Bearing
08/24/2020
EGN3214 - Assignment 1

Calulate the Distance in kilometers, and return the angle of the bearing in degrees.

Variables:

e1, n1 - Starting Point
e2, n2 - End Point
b - Bearing in degrees
d - Distance in kilometers
eastings - Distance traveled or measured eastward
northings - Distance traveled or measured northward
quadrent - What quadrent the bearing is in

Quad Setup for Bearings
        360°        0°
    (4) E-, N+      |   (1) E+, N+
        360+Bearing |       No Change
                    |
270° --------------------------------- 90°
    (3) E-, N-      |   (2) E+, N-
        Bearing-180 |       180+Bearing
                    |
                   180°
'''
import math

def calculateDB(e1, n1, e2, n2):

    b = 0
    d = math.sqrt((n2-n1)**2+(e2-e1)**2)/1000
    eastings = e2-e1
    northings = n2-n1

    if eastings > 0 and northings > 0:
        quadrant = 'First Quadrant E+, N+'
        b = math.degrees(math.atan((e2-e1)/(n2-n1)))
    elif eastings > 0 and northings < 0:
        quadrant = 'Second Quadrant E+, N-'
        b = 180+math.degrees(math.atan((e2-e1)/(n2-n1)))
    elif eastings < 0 and northings < 0:
        quadrant = 'Third Quadrant E-, N-'
        b = 180+math.degrees(math.atan((e2-e1)/(n2-n1)))
    elif eastings < 0 and northings > 0:
        quadrant = 'Fourth Quadrant E-, N+'
        b = 360 + math.degrees(math.atan((e2-e1)/(n2-n1)))

    return d, b, eastings, northings, quadrant
'''
Either calls all coordinates listed in the assignment with a traveled distance or
allows the user to input two sets of coordinates. Then prints the output to the terminal.
'''
def outputAnswers(question, des):

    if question == 'A':
        
        print(des)
        print(quadrant)
        print(f'Eastings {eastings}')
        print(f'Northings {northings}')
        print(f'Distance: {d:.3f} kilometers\nBearing: {b:.3f}\xb0 Degrees')
        print()

    if question == 'M':

        print()
        print('#'*50)
        print()
        print(quadrant)
        print(f'Eastings {eastings}')
        print(f'Northings {northings}')
        print(f'Distance: {d:.3f} kilometers\nBearing: {b:.3f}\xb0 Degrees')
        print()
        print('#'*50)

while True:
    question = input('Enter Eastings and Northings (M)anually or use (A)ssignment Coordinates (M or A)?').upper()

    if question == 'A':
        coordlist = [
        [511005, 3208379, 509938, 3208346, 'Browns Bay Canoe Launch to Sign 3/8'],
        [509938, 3208346, 509948, 3208025, 'Sign 3/8 to Sign 4/7'],
        [509948, 3208025, 510284, 3208171, 'Sign 4/7 to Sign 5/6'],
        [510284, 3208171, 510397, 3208018, 'Sign 5/6 to Sign 6/5'],
        [510397, 3208018, 511005, 3208379, 'Sign 6/5 to Browns Bay Canoe Launch'],
        ]

        totaldist = []
        print() # Blank line to Start
        print('#'*50)
        for item in coordlist:
            
            d, b, eastings, northings, quadrant = calculateDB(item[0], item[1], item[2], item[3])
            question = outputAnswers('A', item[4])

            totaldist.append(d)  
            
        print(f'Total Traveled Distance is {sum(totaldist):.3f} kilometers')
        print('#'*50)
        break
    elif question == 'M':
        e1 = int(input('Enter Eastings Starting Point: '))
        n1 = int(input('Enter Northings Starting Point: '))
        e2 = int(input('Enter Eastings Ending Point: '))
        n2 = int(input('Enter Northings Ending Point: '))

        d, b, eastings, northings, quadrant = calculateDB(e1, n1, e2, n2)
        question = outputAnswers('M', None)
        break
    else:
        print('Enter a valid option.')

