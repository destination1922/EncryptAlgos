from random import randint
alifbo = 'abcdefghijklmnopqrstuvwxyz'
def find_num(k, m, r):
    x = 0
    while x * k % m != r: x += 1
    return x
def encrypt(text, e, n):
    result = ''
    for char in text:
        up = False
        if not char.isalpha(): result += char
        else:
            if char.isupper(): up = True
            sym = alifbo[alifbo.index(char.lower()) ** e % n % 26]
            if up: result += sym.upper()
            else: result += sym
    return result
def decrypt(text, d, n):
    result = ''
    for char in text:
        up = False
        if not char.isalpha(): result += char
        else:
            if char.isupper(): up = True
            sym = alifbo[alifbo.index(char.lower()) ** d % n % 26]
            if up: result += sym.upper()
            else: result += sym
    return result
def mutual_prime(fx):
    prime_nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    e = prime_nums[randint(0, 24)]
    if e < fx: return e
    else: return mutual_prime(fx)
while True:
    selection = input('Are you going to send or recieve message? (enter se or re )\t')
    if selection == 'se':
        print('Ok! You are going to send message')
        text = input('Enter your message:\t')
        e, n = map(int, input('Please enter recieved e and n: \t').split())
        input_text = encrypt(text, e, n)
        print(f"Encrypted message:\t{input_text}")
    else:
        print('Ok! You are going to recieve message')
        p_a = [3, 5, 7, 11, 13, 17, 19, 23, 29]
        p_b = [31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        # p, q = p_a[randint(0, 8)], p_b[randint(0, 15)]
        p, q = map(int, input('p va q ni kiriting:\t').split())
        n = p * q
        fx = (p-1) * (q-1)
        # e = mutual_prime(fx)
        e = int(input(f"{fx} dan kichik tub son kiriting:\t"))
        de = find_num(e, fx, 1)
        print(de)
        print(f"e = {e}, n = {n}. Send these keys")
        encrypted_text = input(f'Enter the encrypted message:\t')
        decrypted_text = decrypt(encrypted_text, de, n)
        print(f'Decrypted message:\t{decrypted_text}')