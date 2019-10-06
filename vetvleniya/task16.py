a = []
for i in range(len(a)):
    a.append(int(input().split()))
for i in range(len(a)):
    if a[i]==a[i+1]:
        n+=1
print(n)
