plaintext = (input("Enter Plain text : "))
ciphertext = (input("Enter Cipher text : "))
# key = int(input("Enter key : "))
key = 0
# cpcc
result = ciphertext
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
    if(str(result2).upper() == str(plaintext).upper()):
        print("Found key= "+str(i)+" = " + result2)
        key = i
        break


newplaintext = (input("Enter New Plain text : "))

newplaintext = newplaintext.upper()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""


for letter in newplaintext:
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
