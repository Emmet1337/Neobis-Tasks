a = int(input())
b = a % 10
c = (a%100-b)
d = (a-b-c)
print(d//100, c//10, b,sep=", ")
