a = int(input())
if a>0 and a<4 or a==12:
    print('Winter')
if a>=4 and a<6:
    print('Spring')
if a>=6 and a<8:
    print('Summer')
if a>=8 and a<12:
    print('Autumn')
if a<1 or a>12:
    print('Wrong number')