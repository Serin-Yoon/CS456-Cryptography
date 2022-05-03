plain = "You are reading the plain text message of our first assignment in cryptography. For the first part of this assignment email this plain text file and describe the substitution cipher used for encryption. For the second part implement a different secret key encryption and decryption scheme for text files and submit your source along with documentation and testing for your implementation using a programming language of your choice. For the third part determine the statistical profiles of english and another language by writing a program to compute their entropies over a large text corpus does the second language have a higher entropy than english. This assignment is due by the middle of February."
c = ''
ac = 0
secretKey = 12 # Secret key that Alice and Bob share

def encrypt(plain):
    encrypted = ""
    for i in range(len(plain)):
        c = plain[i]
        ac = ord(c)
        ac += secretKey
        c = chr(ac)
        encrypted += c
    return encrypted

def decrypt(encrypted):
    decrypted = ""
    for i in range(len(encrypted)):
        c = encrypted[i]
        ac = ord(c)
        ac -= secretKey
        c = chr(ac)
        decrypted += c
    return decrypted


#### Original Text ####
print("[Plain Text]")
print(plain)
print()

#### Encryption (Alice) ####
print("[Encrypted Text]")
encrypted = encrypt(plain)
print(encrypted)
print()

#### Decryption (Bob) ####
print("[Decrypted Text]")
decrypted = decrypt(encrypted)
print(decrypted)
print()

#### Check Validation ####
print("[Original Text = Decrypted Text]")
print(plain == decrypted)
