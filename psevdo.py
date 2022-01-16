# def davri(numbers):
#     array = list(numbers.split())
#     return len(set(array))
# def psevdo_funksiya(a, b, c, d, m, n):
#     x = 0
#     sonlar = ''
#     for _ in range(n):
#         x = int(x)
#         x = str((a*(x**3) + b*(x**2) + c*x + d) % m)
#         sonlar += ' ' + x
#     return sonlar
#
# a, b, c, d, m = map(int, input('Parametrlarni kiriting:\t').split())
# n = int(input("Nechta son generatsiya qilmoqchisiz:\t"))
# generatsiyalangan_sonlar = psevdo_funksiya(a, b, c, d, m, n)
# print(f"Generatsiyalangan sonlar:\t{generatsiyalangan_sonlar}")
# print(f"Davri:\t{davri(generatsiyalangan_sonlar)}")

# import hashlib
#
# # encoding GeeksforGeeks using md5 hash
# # function
# result = hashlib.md5(b'GeeksforGeeks')
#
# # printing the equivalent byte value.
# print("The byte equivalent of hash is : ", end="")
# print(result.digest())
# print()

import hashlib
text = input('Text:\t')
result = hashlib.md5(text.encode())
print(f"Hash qiymat : {result.hexdigest()}")