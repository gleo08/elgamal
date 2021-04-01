import math
import random
import private
import public


def gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = gcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modInv(a, m):
    g, x, y = gcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def genPublicKey():
    publicKey = []
    alpha = public.ALPHA
    p = public.P
    beta = pow(alpha, private.KEY) % p
    publicKey.append(p)
    publicKey.append(alpha)
    publicKey.append(beta)
    return publicKey


def encrypt(k):
    result = []
    encoded = private.ENCODED
    publicKey = genPublicKey()
    y1 = pow(publicKey[1], k) % publicKey[0]
    y2 = (encoded * pow(publicKey[2], k)) % publicKey[0]
    result.append(y1)
    result.append(y2)
    return result

def decrypt(y1, y2):
    p = public.P
    tmp = modInv(pow(y1, private.KEY), p)
    result = (y2*tmp) % p
    return result

print("Message encoded:", private.ENCODED)
print("p:", public.P)
cypher = encrypt(853)
print("Cypher:", cypher)
plaintext = decrypt(cypher[0], cypher[1])
print("Plaintext: ", plaintext)

