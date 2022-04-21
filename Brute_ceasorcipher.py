plaintext = (input("Enter Plain text : "))
key = int(input("Enter key : "))

plaintext = plaintext.upper()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""


for letter in plaintext:
    if letter in alphabet:
        letter_index = (alphabet.find(letter)+key) % len(alphabet)
        result = result + alphabet[letter_index]
    else:
        result = result + letter


print("Encrypted Text = " + result)


encrypted_text = result
encrypted_text = encrypted_text.upper()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result2 = ""

for letter in encrypted_text:
    if letter in alphabet:
        letter_index1 = (alphabet.find(letter)-key) % len(alphabet)
        result2 = result2 + alphabet[letter_index1]
    else:
        result2 = result2 + letter

print("Decrypted Text = " + result2)

# BRUTE FORCE
for i in range(1, 26):
    encrypted_text = result
    encrypted_text = encrypted_text.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result2 = ""

    for letter in encrypted_text:
        if letter in alphabet:
            letter_index1 = (alphabet.find(letter)-i) % len(alphabet)
            result2 = result2 + alphabet[letter_index1]
        else:
            result2 = result2 + letter
    print("Brute force  key= "+i+" = " + result2)
