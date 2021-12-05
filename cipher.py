shift = int(input())
cipher = input()
char1 = 0
for c in range(len(cipher)):
    char1 = ord(cipher[c])
    print(chr(char1 - shift), end = '')