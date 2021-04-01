KEY = 888

def laTinToInt(m):
    encoded = 0
    i = 0
    result = []
    for character in m:
        number = ord(character) - 97
        result.append(number)
    for n in result:
        encoded = encoded + pow(26, i) * n
        i += 1
    return encoded

MESSAGE = 'viecbanthankhongmuonlamthikhonglam'
ENCODED = laTinToInt(MESSAGE)
