alifbo = 'abcdefghijklmnopqrstuvwxyz'
def find_num(k, m, r):
    x = 0
    while x * k % m != r:
        x += 1
    return x
def Affin(text, key_a, key_b, action):
    result = ''
    a = find_num(key_a, 26, 1)
    for char in text:
        up = False
        if not char.isalpha(): result += char
        else:
            if char.isupper(): up = True
            if action == 'encr': sym = alifbo[(key_a * alifbo.index(char.lower()) + key_b) % 26]
            else: sym = alifbo[(a * (alifbo.index(char.lower()) - key_b)) % 26]
            if up: result += sym.upper()
            else: result += sym
    return result
while True:
    a, b = map(int, input("\nEnter the keys a and b:\t").split())
    input_text = input("\nEnter text to encrypt:\t")
    encryption_text = Affin(input_text, a, b, 'encr')
    print(f"\nEncryption text:\t{encryption_text}")
    decryption_text = Affin(encryption_text, a, b, 'decr')
    print(f"\nDecryption text:\t{decryption_text}")