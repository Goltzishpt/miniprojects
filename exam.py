n = int(input())
l = []
for i in range(n):
    x = int(input())
    l.append(x)
del l[l.index(min(l))]
del l[l.index(max(l))]
print(*l, sep = '\n')