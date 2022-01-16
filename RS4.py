while True:
    def fill_key(key):
        result = []
        i = 0
        while i < 256:
            result.append(ord(key[i % len(key)]))
            i += 1
        return result


    def text_to_ord(text):
        result = []
        i = 0
        while i < len(text):
            result.append(ord(text[i]))
            i += 1
        return result


    def main_func(t, s=list(range(256))):
        i = j = 0
        while i < 256:
            j = (j + s[i] + t[i]) % 256
            s[i] = s[i] + s[j]
            s[j] = s[i] - s[j]
            s[i] = s[i] - s[j]
            i += 1


    def RS4_function(text, key, s=list(range(256))):
        t = fill_key(key)
        main_func(t)
        i = j = 0
        result = ''
        for _ in text_to_ord(text):
            i = (i + 1) % 256
            j = (j + s[i]) % 256
            s[i] = s[i] + s[j]
            s[j] = s[i] - s[j]
            s[i] = s[i] - s[j]
            T = (s[i] + s[j]) % 256
            result += chr(s[T] ^ _)
        return result


    plain_text = input("Enter your plain text:\t")
    key = input("Enter the key:\t")

    encryption_text = RS4_function(plain_text, key, list(range(256)))
    print(f'Encryption text:\t{encryption_text}\n')

    decryption_text = RS4_function(encryption_text, key, list(range(256)))
    print(f"Decryption text:\t{decryption_text}\n")
