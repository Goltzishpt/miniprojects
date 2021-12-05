A = int(input())  # менее это недосып
B = int(input())  # больше это пересып
H = int(input())  # сколько она спит
if H < A:
	print('Недосып')
elif H > B:
	print('Пересып')
else:
	print('Это нормально')