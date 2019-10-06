import math
x1,y1,x2,y2,x3,y3 = map(float, input().split())
d1 = math.sqrt(pow(x2-x1, 2)+pow(y2-y1, 2))
d2 = math.sqrt(pow(x3-x2, 2)+pow(y3-y2, 2))
d3 = math.sqrt(pow(x3-x1, 2)+pow(y3-y1, 2))
p = d1+d2+d3
s = math.fabs(0.5*(((x1-x3)*(y2-y3))-((y1-y3)*(x2-x3))))
print('{0:.5f}'.format(p),s)