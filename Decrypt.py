"""Bruteforce Attack"""
def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shifted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

ciphertext = """o ymnx nx ymj ktwjxy uwnrjafq"""

# Try all possible shifts (0 to 25)
for shift in range(26):
    decrypted_text = caesar_decrypt(ciphertext, shift)
    print(f"Key {shift}, plaintext: {decrypted_text}")
