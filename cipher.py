# ЦИФР ЦЕЗАРЯ со сдвигом, только для маленьких буека


shift = int(input()) # цифра сдвига
cipher = input() # шифр
char1 = 0 # значение буквы по юникоду
for c in range(len(cipher)): # цикл по ренжу
    char1 = ord(cipher[c]) # перевод в цифру юникода
    print(chr(char1 - shift), end = '') # принт буквы через цифру
