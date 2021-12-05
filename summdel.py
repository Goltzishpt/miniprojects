# Code_1
# Код находит натуральное число из отрезка [a; b] с максимальной суммой делителей и сумму делителей

a, b = int(input()), int(input())
max_sum = 0
max_digit = 0
for i in range(a, b + 1):
	summ = 0
	for j in range(1, i + 1):
		if a % j == 0:
			summ += j
	a += 1
	if summ >= max_sum:
		max_sum = summ
		max_digit = i
print(max_digit, max_sum)
