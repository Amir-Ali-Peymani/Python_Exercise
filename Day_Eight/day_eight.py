# 1.have a list of the alphabet
# 2.have a list of the decrypt alphabet
# 3. a->alphabet z->decrypt alphabet
#    have the index of a find that in the decrypt
#    store it in the decrypt variable
alphabet = ['a', 'b', ' ', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
decrypt =  ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', ' ']

message = input("what is your message? \n")

def decrypting(message):
    decrypt_message = ""
    for letter in range(len(message)):
        for character in range(len(alphabet)):
            if message[letter] == alphabet[character]:
                decrypt_message += decrypt[character] 
    return decrypt_message

print(decrypting(message))