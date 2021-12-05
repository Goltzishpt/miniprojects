# Code
# Equation Root search program
# a != 0
a = float(input())
b = float(input())
c = float(input())
d = b**2 - (4 * a * c)
x1 = (-b - (d**0.5)) / (2 * a)
x2 = (-b + (d**0.5)) / (2 * a)
if d > 0:
	print(min(x1, x2), max(x1, x2), sep = "\n")
elif d == 0:
	print(-(b / 2 * a))
elif d < 0:
	print("Нет корней")