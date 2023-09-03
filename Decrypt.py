def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                shifted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                shifted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

ciphertext = """WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ"""

# Try all possible shifts (0 to 25)
for shift in range(26):
    decrypted_text = caesar_decrypt(ciphertext, shift)
    print(f"Shift {shift}: {decrypted_text}")

