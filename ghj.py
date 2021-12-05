n = int(input())
while n > 9:
    n = n // 10 + n % 10
print(n)