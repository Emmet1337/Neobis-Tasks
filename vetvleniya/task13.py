import math
n, a1, d = map(int, input().split())
an = a1 + (n-1)*d
sn = ((a1 + an)/2)*n
sn = sn/n
print(math.trunc(sn))