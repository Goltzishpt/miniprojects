a = float(input('Enter digit: '))
b = float(input('Enter digit: '))
c = str(input('Enter function(+, -, /, *, mod(%), pow(**), div(//): '))
if c == "mod" and b != 0:
	print(a % b)
elif c == "pow":
	print(a ** b)
elif c == "div" and b != 0:
	print(a // b)
elif c == "-":
	print(a - b)
elif c == "+":
	print(a + b)
elif c == "*":
	print(a * b)
elif c == "/" and b != 0:
	print(a / b)
else:
	print("На ноль не делим!")