import sys

input = sys.argv[1:]
text = input[0].strip()
step = int(input[1].strip())
cipher_text = ""

for ch in text:
    shiffer_character_code = ord(ch) + step
    if ch.isupper():
        if shiffer_character_code > 90:
            shiffer_character_code = (shiffer_character_code % 90) + 65
        cipher_text += chr(shiffer_character_code)
    if ch.lower():
        if shiffer_character_code > 122:
            shiffer_character_code = (shiffer_character_code % 122) + 97
        cipher_text += chr(shiffer_character_code)

print(cipher_text)
