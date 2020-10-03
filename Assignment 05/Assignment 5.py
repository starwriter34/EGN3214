'''
Chris Oakley
Functions Part 1
09/13/2020
EGN3214 - Assignment 5

Variables:

n - is Manning's n for roughness of the bottom of the channel
b - Bottom width of channel (ft)
y - Depth of Channel (ft)
z - Side slope of the channel (horizontal)
s - Directional slope of the channel
error - The Step interval for the interation
array - The Array the promel iterates though 0-5

Q - The Flow of the Channel in (cfs - cubic feet/sec)
start - Start time saved
inches - Q is converted to remaining inches 
feet - Q is converted to whole feet

'''
import math
import numpy as np
import time

def TrapezoidalQ(n,b,y,z,s):
   # n is Manning's n - table at 
   # https://www.engineeringtoolbox.com/mannings-roughness-d_799.html
   # b = Bottom width of channel (ft)
   # y = Depth of channel (ft)
   # z = Side slope of channel (horizontal)
   # s = Directional slope of channel - direction of flow
   A = b*y + z*y*y
   W = b + 2*y*math.sqrt(1 + z*z)
   R = A/W
   Q = 1.49/n * A * math.pow(R, 2.0/3.0) * math.sqrt(s)
   return Q

error = 0.0001
b = 3
z = 2
s = 0.01
n = 0.022

start = time.time()
array = np.arange(1,2,error)

for i in array:
    
    Q = TrapezoidalQ(n, b, i, z, s)
    
    feet = math.floor(i)
    inches = (i * 12) % 12

    if Q >= 50:
        print(f'At {Q:.10f} cfs the depth of the channel is {feet:.2f} feet, {inches:.2f} inches!')
        print(f'Took {(time.time()-start)*1000:.2f} milliseconds to find the answer.')
        break