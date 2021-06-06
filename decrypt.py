import sympy
import math

def decrypt_byte(cipherByte, privateKey, publicKey):
    #unpack public Key
    N = publicKey[0]
    encryptionExponent = publicKey[1]
    #unpack private key
    p = privateKey[0]
    q = privateKey[1]
    #calculate decryption exponent
    d = sympy.mod_inverse(encryptionExponent, ((p-1)*(q-1)))
    #decrypt and return
    originalByte = pow(int(cipherByte), d, N)
    return originalByte

def decrypt_file(privateKey, publicKey):
    #open files
    ciphertext = open("encryptedFile.txt", "r")
    decryptedFile = open("decryptedFile.txt", "w")
    #iterate over each byte in the file
    for cipherByte in ciphertext:
        #strip off the newline character
        cipherByte = cipherByte.strip()
        #decrypt byte
        decrypted_byte = decrypt_byte(cipherByte, privateKey, publicKey)
        #write byte to ciphertext file
        decryptedFile.write(chr(decrypted_byte))
    #close files
    ciphertext.close()
    decryptedFile.close()

privateKey = [None, None]
publicKey = [None, None]
#get the public key and private key from the user
privateKey[0] = int(input('Please enter the first number of your private key \n>'))
privateKey[1] = int(input('Please enter the second number of your private key \n>'))
publicKey[0] = int(input('Please enter the first number of your public key \n>'))
publicKey[1] = int(input('Please enter the second number of your public key \n>'))
#convert private and public keys to tuples
privateKey = tuple(privateKey)
publicKey = tuple(publicKey)
#decrypt file
decrypt_file(privateKey, publicKey)
