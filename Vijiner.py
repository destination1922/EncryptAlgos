a = 'abcdefghijklmnopqrstuvwxyz'
def Vijiner(text, key, action):
    result = ''
    k = 0
    for char in text:
        up = False
        if not char.isalpha(): result += char
        else:
            if char.isupper(): up = True
            if action == 'enc': sym = a[(a.index(char.lower()) + a.index(key[k].lower())) % 26]
            else: sym = a[(a.index(char.lower()) - a.index(key[k].lower())) % 26]
            if up: result += sym.upper()
            else: result += sym
        k += 1
        if k == len(key): k = 0
    return result
while True:
    key = input("\nEnter the key:\t")
    input_text = input("\nEnter text to encrypt:\t")
    encryption_text = Vijiner(input_text, key, 'enc')
    print(f"\nEncryption text:\t{encryption_text}")
    decryption_text = Vijiner(encryption_text, key, 'dec')
    print(f"\nDecryption text:\t{decryption_text}")