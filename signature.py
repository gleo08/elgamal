import public
import private

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

#digital signature
def signature(k):
    p = public.P
    alpha = public.ALPHA
    encoded = private.ENCODED
    a = private.KEY
    result = []
    invK = modInv(k, (p - 1))
    gamma = pow(alpha, k) % p
    phi = ((encoded - a * gamma)*invK) % (p - 1)
    result.append(gamma)
    result.append(phi)
    return result

#signature verify
def verify(gamma, phi):
    alpha = public.ALPHA
    a = private.KEY
    p = public.P
    encoded = private.ENCODED
    beta = pow(alpha, a) % p
    ver1 = (pow(beta, gamma) * pow(gamma, phi)) % p
    ver2 = (pow(alpha, encoded)) % p
    return (ver1 == ver2)

s = signature(853)
print(s)
v = verify(s[0], s[1])
print(v)