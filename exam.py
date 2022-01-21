# на вход подается число n и n чисел, удаляется максимальное и минимальное значние согласно задания 3 в теме 11.4
# проверка связи


l = [int(input()) for _ in range(int(input()))]
print(*list(filter(lambda x: str(x) != str(max(l)) and str(x) != str(min(l)), l)), sep='\n')
