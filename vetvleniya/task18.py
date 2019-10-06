X, Y, Z = map(int, input().split())
if X + Y >= Z and X + Z >= Y and Y + Z >= X:
	print("YES")
else:
	print("NO")