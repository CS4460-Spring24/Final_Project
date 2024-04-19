# this file is a script that runs the functions from ProjectPythonCode.py
# each block of code is related to a particular challenge
# the comments should explain what challenge, and answer
# what the challenge is asking for, as well as other relevant information


from ProjectPythonCode import *


print("\n\nComputations for our computational challenges.")


# Challenge: esy RSA
n1 = 7*17
m1 = 6*16
e1 = 23
d1 = modInverse(e1, m1)
print("\n\nChallenge: easy RSA: private key d = ", d1)


# Challenge: ASC II character challenge
message1 = [83, 101, 97, 110, 32, 116, 104, 101, 32, 98, 108, 97, 99, 107, 32, 99, 97, 116]
string_ASC = ASC_message(message1)
print("\n\nChallenge: ASC II character challenge: string = ", string_ASC)


# CHallenge: medium RSA
# combines RSA and ASC II encoding
message2 = "Sean the Abyssinian cat"
sean_message = message_ASC(message2)
sean_encrypted = encrypt(sean_message)
encrypted_array = [34,  159,  251,  73,   128,  205,  139,  159,  128,  151,  35,  137,  173,  173,  154,  73,  154,  251,  73,  128,  141,  251, 205]
assert sean_encrypted == encrypted_array
n2 = 7*37
m2 = 6*36
e2 = 59
d2 = modInverse(e2, m2)
assert d2 == 11
decrypted_array = decrypt(encrypted_array)
decrypted_message = ASC_message(decrypted_array)
print("\n\nChallenge: medium RSA: private key d = ", d2)
print("Challenge: medium RSA: decrypted message = ", decrypted_message)
# Notes:
# 1. The message is "Sean the Abyssinian cat"
# 2. For the primes involved, 7*37 = 259, the decrypt function
# runs a loop mod 259, and so the ASC_message function would not
# work on all numbers, as ASC encoding is mod 256. 



# Challenge: hard RSA
n3 = 1_000_003 * 1_000_037
m3 = 1_000_002 * 1_000_036
e3 = 10_007
d3 = modInverse(e3, m3)
print("\n\nChallenge: hard RSA: private key d = ", d3)


# Challenge: medium Diffie-Hellman
# checking 5 is a primitive root of the prime 10007
g = 5
temp = 1
index = 1
for i in range(1, 10007):
    temp = (temp * g) % 10007
    if temp == 1:
        index = i
        break
print("\n\nChallenge: medium Diffie-Hellman: 5 is a primitive root of 10007")
print("the smallest power n so that 5^n = 1 (mod 10007) is: ", index)
a = 17
b = 71
product = 1
for i in range(a * b):
    product = (product * 5) % 10007
print("Alice's private key is: ", a)
print("Bob's private key is: ", b)
print("the shared secret key is: ", product)


# Challenge: medium Diffie-Hellman #2
# This is a code challenge: the user is supposed to produce
# similar code, and print(primitive_root) at the end
# so stdout can read it
prime1 = 191
primitive_root = 0
for g in range(2, prime1):
    temp = 1
    power = 1
    for i in range(1, prime1):
        temp = (temp * g) % prime1
        if temp == 1 and i < prime1 - 1:
            break
        elif temp == 1 and i == prime1 - 1:
            power = i
            break
    if power == 190:
        primitive_root = g
        break
print("\n\nChallenge: medium Diffie-Hellman #2: with prime 191")
print("the smallest elemnt g so that the smallest power")
print("n so that g^n = 1 (mod 191) is n = 190 is:  g =", primitive_root)


