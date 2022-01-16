a = 'abcdefghijklmnopqrstuvwxyz'
def Sezar_encryption(text, key, action):
    result = ''
    for char in text:
        if not char.isalpha(): result += char
        else:
            if action == 'encr': sym = a[(a.index(char.lower()) + key) % 26]
            else: sym = a[(a.index(char.lower()) - key) % 26]
            if char.isupper(): result += sym.upper()
            else: result += sym
    return result
while True:
    key = int(input("\nEnter the key:\t")) % 26
    input_text = input("\nEnter text to encrypt:\t")
    encryption_text = Sezar_encryption(input_text, key, 'encr')
    print(f"\nEncryption text:\t{encryption_text}")
    decryption_text = Sezar_encryption(encryption_text, key, 'decr')
    print(f"\nDecryption text:\t{decryption_text}")