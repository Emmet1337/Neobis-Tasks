a =  list(map(int, input().split()))
max = 0
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
        maxIndex = i
print(max)
