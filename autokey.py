def encrypt(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha:
            letter_index = (alpha.find(letter) + key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

def decrypt(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha:
            letter_index = ((alpha.find(letter) - key)+26) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter 

    return result



# ENCRYPTION
plainText=input("Enter Plain Text : ")
key1="B"
newkey = key1+plainText 
print(newkey)
ciphert = ""
for i in range(0,len(plainText)):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    newkey[i].upper()
    for letter in newkey[i]:
        letter=letter.upper()
        # print(letter)
        if letter in alpha:
            letter_index = (alpha.find(letter)) % len(alpha)
            ciphert = ciphert+encrypt(letter_index, plainText[i])
            # print(letter_index)
            # print(letter_index)
    # print(encrypt(letter_index, plainText[i]))

print("CIPHER TEXT : "+ ciphert)



#DECRYPTION
key1="B"
newkey = key1+ciphert
print(newkey)
# print(newkey)
plaint = ""
for i in range(0,len(ciphert)):
    # print(plainText[i]+" "+newkey[i])
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    newkey[i].upper()
    for letter in newkey[i]:
        if letter in alpha:
            letter_index = (alpha.find(letter)) % len(alpha)
            plaint = plaint+decrypt(letter_index, ciphert[i])
            # print(letter_index)
    # print(encrypt(letter_index, plainText[i]))
print("PLAIN TEXT : "+ plaint)
