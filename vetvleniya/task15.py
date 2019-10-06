a, b, c = map(int, input().split())
max = 0
min = 0
n = 0
if a > b:
    max = a
else:
    max = b
if c > max:
    max = c
if a < b:
    min = a
else:
    min = b
if c < min:
    min = c
if a == max:
    n = n+1
if b == max:
    n = n+1
if c == max:
    n = n+1
if n == 3:
    print('Same age')
if n == 2:
    if  a == min:
        print("Anton")
    if  b == min:
        print('Boris')
    if  c == min:
        print('Victor')
if n == 1:
    if a == max:
        print("Anton")
    if b == max:
        print('Boris')
    if c == max:
        print('Victor')
