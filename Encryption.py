import random
import string

code = string.punctuation + string.digits + string.ascii_letters
chars = list(code)
key = chars.copy()

random.shuffle(key)
print(f"chars: {code}")
print(f"key: {key}")

# for encrypt
plain_text = input("Enter a word to encrypt:")
word_text = ""

for word in plain_text:
    index = chars.index(word)
    word_text += key[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {word_text}")

# for decrypt
word_text = input("Enter a word to decrypt:")
plain_text = ""

for word in word_text:
    index = key.index(word)
    plain_text += chars[index]
    
print(f"encrypted message: {word_text}")
print(f"original message: {plain_text}")

