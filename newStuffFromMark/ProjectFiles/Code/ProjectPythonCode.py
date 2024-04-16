

# this fucntion takes 2 positive integers and returns their gcd
def gcdExtended(a, b):
    global x, y
 
    # Base Case
    if (a == 0):
        x = 0
        y = 1
        return b
 
    # To store results of recursive call
    gcd = gcdExtended(b % a, a)
    x1 = x
    y1 = y
 
    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1
 
    return gcd
 
 
 # this function takes 2 positive integers and returns the modular
 # inverse of the first number mod the second number
 # if the inverse does not exist, the function returns None
def modInverse(A, M):
 
    g = gcdExtended(A, M)
    if (g != 1):
        print("Inverse doesn't exist")
        return None
    else:
 
        # m is added to handle negative x
        res = (x % M + M) % M
        # print("Modular multiplicative inverse is ", res)
        return res


# backup gcd function
def gcdExtended2(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = gcdExtended2(b % a, a)
        return gcd, y - (b // a) * x, x

# backup modInverse function
def modInverse2(A, M):
    g, x, _ = gcdExtended2(A, M)
    if g != 1:
        print("Inverse doesn't exist")
        return None
    else:
        # m is added to handle negative x
        res = (x % M + M) % M
        # print("Modular multiplicative inverse is ", res)
        return res



# this function takes a string and returns a list of the ASCII 
# values of the characters in the string
def message_ASC(string):
    #message = []
    #for char in string:
    #    order = ord(str(char))
    #    message.append(order)
    #return message
    return [ord(char) for char in string]

# this function takes a list of ASCII values and returns the
# corresponding string
def ASC_message(message):
    string = ''
    for order in message:
        char = chr(order)
        string += char
    return string


# this function takes a list of numbers and encrypts them
# this is specific to the RSA encryption for the
# medium RSA challenge
def encrypt(array):
    encrypt = []
    for num in array:
        temp = 1
        for i in range(59):
            temp = (temp * num) % 259
        encrypt.append(temp)
    return encrypt


# this function takes a list of numbers and decrypts them
# this is specific to the RSA encryption for the
# medium RSA challenge
def decrypt(array):
    decrypt = []
    for num in array:
        temp = 1
        for i in range(11):
            temp = (temp * num) % 259
        decrypt.append(temp)
    return decrypt


# checking code
# sean = "Sean the Abyssinian cat"
# sean_message = message_ASC(sean)
# sean_encrypted = encrypt(sean_message)
# sean_decrypted = decrypt(sean_encrypted)
# decrypted_sean = ASC_message(sean_decrypted)
# print(decrypted_sean)

