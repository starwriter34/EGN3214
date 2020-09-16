import math
numbreak = 1000

for a in range(1,numbreak):
    for b in range(a,numbreak):
        for c in range(b,numbreak):
            if (a+b+c)==numbreak and (a**2+b**2)==c**2:
                print(a*b*c)
                break
# 31875000
# n = 100

# for b in range(n):
#     for a in range(1, b):
#         c = math.sqrt( a * a + b * b)
#         if c % 1 == 0:
#             print(a, b, int(c))