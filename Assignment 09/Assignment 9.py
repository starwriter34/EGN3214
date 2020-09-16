import math
import time
numbreak = 1000
start = time.time()
break_for = False

for a in range(1,numbreak):
    for b in range(a+1,numbreak):
        for c in range(b+1,numbreak):
            if (a+b+c)==numbreak and (a**2+b**2)==c**2:
                print(a*b*c)
                print(f'Time Taken {time.time()-start} in seconds!')
                break_for = True
            
        if break_for == True:
            break
    if break_for == True:
        break

# 31875000
# n = 100

# for b in range(n):
#     for a in range(1, b):
#         c = math.sqrt( a * a + b * b)
#         if c % 1 == 0:
#             print(a, b, int(c))