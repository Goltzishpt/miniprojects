import random

def password_generation(chars):
    password = ''
    for i in range(random.randint(8, 15)):
        password += random.choice(chars)
    return password
chars = '!#$%&*+-=?@^_.ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
while True:
    print(password_generation(chars))