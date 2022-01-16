d = {
    'a': 0b00000, 'b': 0b00001, 'c': 0b00010, 'd': 0b00011, 'e': 0b00100, 'f': 0b00101, 'g': 0b00110, 'h': 0b00111,
    'i': 0b01000, 'j': 0b01001, 'k': 0b01010, 'l': 0b01011, 'm': 0b01100, 'n': 0b01101, 'o': 0b01110, 'p': 0b01111,
    'q': 0b10000, 'r': 0b10001, 's': 0b10010, 't': 0b10011, 'u': 0b10100, 'v': 0b10101, 'w': 0b10110, 'x': 0b10111,
    'y': 0b11000, 'z': 0b11001, '?': 0b11010, '!': 0b11011, "'": 0b11100, '.': 0b11101, ',': 0b11110, ' ': 0b11111,
}
def a_bin(char):
    return d[char.lower()]
def bin_a(n):
    for i in d.keys():
        if d[i] == n: return i
def VernamCipherFunction(text, key):
    result = ""
    ptr = 0
    for char in text:
        up = False
        if char.isupper(): up = True
        sym = bin_a(a_bin(char) ^ a_bin(key[ptr]))
        if up:
            result += sym.upper()
        else:
            result += sym
        ptr += 1
        if ptr == len(key):
            ptr = 0
    return result
encryption_key = input("\nEnter encryption key:\t")
while True:
    input_text = input("\nEnter Text To Encrypt:\t")
    encryption = VernamCipherFunction(input_text, encryption_key)
    print("\nEncrypted Vernam Cipher Text:\t" + encryption)
    decryption = VernamCipherFunction(encryption, encryption_key)
    print("\nDecrypted Vernam Cipher Text:\t" + decryption)