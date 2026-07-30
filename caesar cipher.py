#Caesar Cipher 
#Encrypt and decrypt a message using the Caesar Cipher algorithm.

text = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

# Encryption
encrypted = ""

for ch in text:
    if ch.isalpha():
        if ch.isupper():
            encrypted += chr((ord(ch) - 65 + shift) % 26 + 65)
        else:
            encrypted += chr((ord(ch) - 97 + shift) % 26 + 97)
    else:
        encrypted += ch

print("Encrypted message:", encrypted)

# Decryption
decrypted = ""

for ch in encrypted:
    if ch.isalpha():
        if ch.isupper():
            decrypted += chr((ord(ch) - 65 - shift) % 26 + 65)
        else:
            decrypted += chr((ord(ch) - 97 - shift) % 26 + 97)
    else:
        decrypted += ch

print("Decrypted message:", decrypted)
