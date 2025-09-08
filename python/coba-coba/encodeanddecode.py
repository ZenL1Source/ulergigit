# Encode: teks -> angka
def encode(text):
    text = text.upper()
    result = []
    for char in text:
        if char.isalpha():  # hanya huruf A-Z
            result.append(str(ord(char) - 64))  # 'A' = 65 di ASCII
        else:
            result.append(char)  # karakter lain (spasi, kurung, dll) biar tetap
    return " ".join(result)

# Decode: angka -> teks
# def decode(code):
#     parts = code.split()
#     result = []
#     for part in parts:
#         if part.isdigit():
#             num = int(part)
#             if 1 <= num <= 26:
#                 result.append(chr(num + 64))  # balik ke huruf
#             else:
#                 result.append('?')  # kalau diluar jangkauan
#         else:
#             result.append(part)  # simbol/karakter khusus tetap
#     return "".join(result)

#Contoh pemakaian:
# decoded = decode(encoded)

text = "Hello World"
encoded = encode(text)
# print("Teks asli :", text)
print("Encoded   :", encoded)
# print("Decoded   :", decoded)
