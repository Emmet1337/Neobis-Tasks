import math
depth = float(input())
radius = depth/2
v = (4/3)*math.pi*pow(radius, 3)
print('{0:.3f}'.format(v))