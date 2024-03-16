import sys

input = sys.argv[1:]
text = input[0].strip()
key = input[1].strip()
key_length = len(key)
cipher_text = ""

for i in range(len(text)):
    key_value = ord(key[i % key_length])
    alphabet = ""
    for j in range(26):
        next_char = key_value + j
        if next_char > 90:
            next_char = (next_char % 90) + 64
        alphabet += chr(next_char)
    search_ch = text[i]
    indexOfSearchCh = ord(search_ch) % 65
    cipher_text += alphabet[indexOfSearchCh]

print(cipher_text)
