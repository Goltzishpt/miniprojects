a = int(input())
b = int(input())
for i in range(a, b + 1):
    counter = 0
    for j in range(2, i + 1):
        if a % j == 0:
            counter += 1
    if counter == 1:
        print(a)
    a += 1