a, b = map(int, input().split())
for i in range(a,b+1):
    c = pow(i, 2)
    print (str(i)+"*"+str(i)+"="+str(c))