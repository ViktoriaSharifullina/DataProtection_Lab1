import os
from collections import defaultdict
from random import shuffle

file_name = "C:\\Users\\vikto\\OneDrive\\Рабочий стол\\ЗИ\\Lab_1\\Document.doc"
file_key = "C:\\Users\\vikto\\OneDrive\\Рабочий стол\\ЗИ\\Lab_1\\key.txt"
test = "C:\\Users\\vikto\\OneDrive\\Рабочий стол\\ЗИ\\Lab_1\\test.txt"

file_stats = os.stat(file_name)

print(f'File Size in Bytes is {file_stats.st_size}')
size = file_stats.st_size

with open(file_name, "rb") as file:
    text = file.read()
print("Text before encode/decode  ", text)

dict = defaultdict(float)
for char in text:
    dict[char] += 1
for key in dict:
    dict[key] = dict[key] / size

print("Relative Frequencies :  ", dict)


def write_random_keys(fk_path):
    keys = list(range(0, 256))
    with open(fk_path, "wb") as f:
        shuffle(keys)
        byteKeys = bytes(keys)
        f.write(byteKeys)


def read_random_key(fk_path):
    with open(fk_path, 'rb') as f:
        data = f.read()
    return data


def remove_char(s):
    result = s[1: -1]
    return result


def encode(fk_path, fd_path):
    encode_text = []
    key = read_random_key(fk_path)

    with open(fd_path, "rb") as frb:
        text = frb.read()
    for c in text:
        encode_text.append(key[c])
    print("Encode text ", bytes(encode_text))
    with open(fd_path, "wb") as fwb:
        fwb.write(bytes(encode_text))


def decode(fk_path, fd_path):
    decode_text = []
    key = read_random_key(fk_path)
    with open(fd_path, "rb") as frb:
        text = frb.read()
    for t in text:
        for i in range(len(key)):
            if t == key[i]:
                decode_text.append(i)

    print("Decode text ", bytes(decode_text))
    with open(fd_path, "wb") as fwb:
        fwb.write(bytes(decode_text))


write_random_keys(file_key)
encode(file_key, file_name)
decode(file_key, file_name)
