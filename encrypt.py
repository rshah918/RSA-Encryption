'''
RSA Encryption:

Key Creation:
    1) Choose secret primes p and q
    2) Choose encryption exponent e such that gcd(e, (p-1)(q-1)) = 1
    3) Publish N=p*q and e
Encryption:
    1) ciphertext = m^e (mod N)

Decryption:
    1) Compute d such that d = e^-1 (mod (p-1)(q-1))
    2) original message = c^d (mod N)

'''

import random
import math
import sympy
import sys
from sympy.ntheory.primetest import isprime

#publish public key
    #choose primes
    #choose e
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def generate_primes():
    p = 903143
    q = 901499
    while (p == None) or (q==None):
        odd_rand_num = random.randrange(100000,999999)
        if isprime(odd_rand_num):
            if p == None:
                p = odd_rand_num
            else:
                q = odd_rand_num
    print("Your private key is: ", (p,q))
    return (p, q)

def generate_encryption_exponent(privateKey):
    p = privateKey[0]
    q = privateKey[1]
    c = (p-1)*(q-1)

    encryptionExponent = None
    while encryptionExponent == None:
        randInt = random.randrange(0,9999999)
        if math.gcd(randInt, p-1) == 1 and math.gcd(randInt, q-1) == 1:
            encryptionExponent = randInt
    print("Encryption exponent is: ", encryptionExponent)
    d = sympy.mod_inverse(encryptionExponent, c)
    print("D = ", d)
    return encryptionExponent

def generate_public_key():
    privateKey = generate_primes()
    encryptionExponent = generate_encryption_exponent(privateKey)
    N = privateKey[0] * privateKey[1]
    print("Public Key is: ", (N, encryptionExponent))
    return (N, encryptionExponent)

def encrypt_byte(byte, publicKey):
    #unpack public key
    N = publicKey[0]
    encryptionExponent = publicKey[1]
    #interpret each byte as an integer
    int_val = int.from_bytes(byte, "big")
    #encrypt and return
    cipherByte = pow(int_val, encryptionExponent, N)
    return cipherByte

def encrypt_file():
    #generate public key
    publicKey = generate_public_key()
    #open files
    file = open("file-to-encrypt.txt", "rb")
    ciphertext = open("encryptedFile.txt", "w")
    #iterate over each byte in the file
    byte = file.read(1)
    while byte:
        encrypted_byte = encrypt_byte(byte, publicKey)
        #write byte to ciphertext file
        ciphertext.write(str(encrypted_byte))
        #use a newline delimiter
        ciphertext.write('\n')
        #get the next byte
        byte = file.read(1)
    file.close()
    ciphertext.close()
encrypt_file()
