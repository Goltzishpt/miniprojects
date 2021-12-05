a = int(input())
b = int(input())
c = int(input())
if a == b == c: # 1 1 1 
	print(a, b, c)
elif a == b > c: # 2 2 1
	print(a or b, c, a or b)
elif a == b < c: # 1 1 2
	print(c, a or b, a or b)
elif a < b < c: # 1 2 3
	print(c, a, b)
elif a > b > c: # 3 2 1
	print(a, c, b)
elif a > b < c and a < c: # 2 1 3
	print(c, b, a)
elif a > b < c and a > c: # 3 1 2
	print(a, b, c)
elif a < b > c and a < c: # 1 3 2
	print(b, a, c)
elif a < b > c and a > c: # 2 3 1
	print(b, c, a)
elif a < b == c: # 1 2 2
	print(b or c, a, b or c)
elif a > b == c: # 2 1 1
	print(a, b or c, b or c)
elif a == c < b:
	print(b, a or c, a or c)
else:
	print()