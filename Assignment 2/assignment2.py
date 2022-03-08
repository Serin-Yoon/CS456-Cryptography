import sympy
import math

def RSA_Decrypt():
    cipherFile = "cipher.txt"
    publicKeysFile = "publicKeys.txt"

    with open(cipherFile) as file:
        cipher = file.read().splitlines()

    with open(publicKeysFile) as file:
        publicKeys = file.read().splitlines()

    cipher = list(map(int, cipher))
    publicKeys = list(map(int, publicKeys))

    n = publicKeys[0]
    e = publicKeys[1]

    for m in range(0, 127):
        c = pow(m, e, n)
        asciiChr = chr(m)
        #print("%d ^ e mod n → %c" % (m, asciiChr))
        for i, j in enumerate(cipher):
            if j == c:
                cipher[i] = asciiChr

    decrypted = ''.join([x for x in cipher if not isinstance(x, int)])
    print("\n============================ Decrypt ============================")
    print(decrypted, end="")

    with open("decrypted.txt", "w") as file:
        file.write(decrypted)
    file.close()

def createKeys():
    p = sympy.randprime(0, 50)
    q = sympy.randprime(0, 50)
    while p >= q:
        q = sympy.randprime(0, 50)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = findCoprime(phi)
    d = xgcd(phi, e)
    while (d < 0):
        d += phi
    return p, q, n, phi, e, d

def RSA_Encrypt(n, e):
    plainFile = "decrypted.txt"

    with open(plainFile) as file:
        plain = file.read()

    plain = list(plain)

    for i in range(0, len(plain)):
        asciiCode = ord(plain[i])
        c = pow(asciiCode, e, n)
        #print("%c ^ e mod n → %d" % (plain[i], c))
        plain[i] = str(c)

    plain = ' '.join([x for x in plain if not isinstance(x, int)])
    print("=========================== Re-encrypt ===========================")
    print(plain)
    with open("reencrypted.txt", "w") as file:
        file.write(plain)
    file.close()

def findCoprime(a):
    e = 3
    while math.gcd(a, e) != 1:
        e += 2
    return e

def xgcd(a, b):
    prevX, x = 1, 0;
    prevY, y = 0, 1
    while b:
        q = a // b
        x, prevX = prevX - q * x, x
        y, prevY = prevY - q * y, y
        a, b = b, a % b
    return prevY


RSA_Decrypt()  # decrypting
p, q, n, phi, e, d = createKeys()  # create my own keys
RSA_Encrypt(n, e)  # Re-encrypting using my own keys

print("\n============================== keys ==============================")
print('p: %d / q: %d / n: %d / Φ: %d / e: %d / d: %d' % (p, q, n, phi, e, d))