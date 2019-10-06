n = int(input())
i=0
s=0
k=1
num =map(int, input().split(maxsplit = n))
for i in num:
    s += i
if i <=0 or i>=180:
    k=0
print(s)
if k==1:
    if s==180:
        if n==3:
            print("YES")
        else:
            print("NO")
    else:
        if s==180*(n-2):
            print("YES")
        else:
            print("NO")
else:
    print("NO")