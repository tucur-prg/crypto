from bit import rotl32
from util import padding, toStr

H = [
    0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0
]
W = []

def blk0(i):
    global W
    return W[i]

def blk(i):
    global W
    W[i&15] = rotl32( W[(i+13)&15] ^ W[(i+8)&15] ^ W[(i+2)&15] ^ W[i&15], 1)
    return W[i&15]

def R0(v, w, x, y, z, i):
    z += ((w&(x^y))^y) + blk0(i) + 0x5A827999 + rotl32(v, 5)
    w = rotl32(w, 30)
    return [v, w, x, y, z&0xFFFFFFFF]

def R1(v, w, x, y, z, i):
    z += ((w&(x^y))^y) + blk(i) + 0x5A827999 + rotl32(v, 5)
    w = rotl32(w, 30)
    return [v, w, x, y, z&0xFFFFFFFF]

def R2(v, w, x, y, z, i):
    z += (w^x^y) + blk(i) + 0x6ED9EBA1 + rotl32(v, 5)
    w = rotl32(w, 30)
    return [v, w, x, y, z&0xFFFFFFFF]

def R3(v, w, x, y, z, i):
    z += (((w|x)&y)|(w&x)) + blk(i) + 0x8F1BBCDC + rotl32(v, 5)
    w = rotl32(w, 30)
    return [v, w, x, y, z&0xFFFFFFFF]

def R4(v, w, x, y, z, i):
    z += (w^x^y) + blk(i) + 0xCA62C1D6 + rotl32(v, 5)
    w = rotl32(w, 30)
    return [v, w, x, y, z&0xFFFFFFFF]

def block(H, padding):
    N = len(padding) // 64

    W = list(range(80))
    for i in range(1, N+1):
        for t in range(16):
            p = (i - 1) * 64 + t * 4
            W[t] = int.from_bytes(padding[p:p+4], 'big')

        H = transform(H, W)
    return H

def transform(H, _W):
    global W
    W = _W

    a, b, c, d, e = H
    a, b, c, d, e = R0(a, b, c, d, e, 0)
    e, a, b, c, d = R0(e, a, b, c, d, 1)
    d, e, a, b, c = R0(d, e, a, b, c, 2)
    c, d, e, a, b = R0(c, d, e, a, b, 3)
    b, c, d, e, a = R0(b, c, d, e, a, 4)
    a, b, c, d, e = R0(a, b, c, d, e, 5)
    e, a, b, c, d = R0(e, a, b, c, d, 6)
    d, e, a, b, c = R0(d, e, a, b, c, 7)
    c, d, e, a, b = R0(c, d, e, a, b, 8)
    b, c, d, e, a = R0(b, c, d, e, a, 9)
    a, b, c, d, e = R0(a, b, c, d, e, 10)
    e, a, b, c, d = R0(e, a, b, c, d, 11)
    d, e, a, b, c = R0(d, e, a, b, c, 12)
    c, d, e, a, b = R0(c, d, e, a, b, 13)
    b, c, d, e, a = R0(b, c, d, e, a, 14)
    a, b, c, d, e = R0(a, b, c, d, e, 15)
    e, a, b, c, d = R1(e, a, b, c, d, 16)
    d, e, a, b, c = R1(d, e, a, b, c, 17)
    c, d, e, a, b = R1(c, d, e, a, b, 18)
    b, c, d, e, a = R1(b, c, d, e, a, 19)

    a, b, c, d, e = R2(a, b, c, d, e, 20)
    e, a, b, c, d = R2(e, a, b, c, d, 21)
    d, e, a, b, c = R2(d, e, a, b, c, 22)
    c, d, e, a, b = R2(c, d, e, a, b, 23)
    b, c, d, e, a = R2(b, c, d, e, a, 24)
    a, b, c, d, e = R2(a, b, c, d, e, 25)
    e, a, b, c, d = R2(e, a, b, c, d, 26)
    d, e, a, b, c = R2(d, e, a, b, c, 27)
    c, d, e, a, b = R2(c, d, e, a, b, 28)
    b, c, d, e, a = R2(b, c, d, e, a, 29)
    a, b, c, d, e = R2(a, b, c, d, e, 30)
    e, a, b, c, d = R2(e, a, b, c, d, 31)
    d, e, a, b, c = R2(d, e, a, b, c, 32)
    c, d, e, a, b = R2(c, d, e, a, b, 33)
    b, c, d, e, a = R2(b, c, d, e, a, 34)
    a, b, c, d, e = R2(a, b, c, d, e, 35)
    e, a, b, c, d = R2(e, a, b, c, d, 36)
    d, e, a, b, c = R2(d, e, a, b, c, 37)
    c, d, e, a, b = R2(c, d, e, a, b, 38)
    b, c, d, e, a = R2(b, c, d, e, a, 39)

    a, b, c, d, e = R3(a, b, c, d, e, 40)
    e, a, b, c, d = R3(e, a, b, c, d, 41)
    d, e, a, b, c = R3(d, e, a, b, c, 42)
    c, d, e, a, b = R3(c, d, e, a, b, 43)
    b, c, d, e, a = R3(b, c, d, e, a, 44)
    a, b, c, d, e = R3(a, b, c, d, e, 45)
    e, a, b, c, d = R3(e, a, b, c, d, 46)
    d, e, a, b, c = R3(d, e, a, b, c, 47)
    c, d, e, a, b = R3(c, d, e, a, b, 48)
    b, c, d, e, a = R3(b, c, d, e, a, 49)
    a, b, c, d, e = R3(a, b, c, d, e, 50)
    e, a, b, c, d = R3(e, a, b, c, d, 51)
    d, e, a, b, c = R3(d, e, a, b, c, 52)
    c, d, e, a, b = R3(c, d, e, a, b, 53)
    b, c, d, e, a = R3(b, c, d, e, a, 54)
    a, b, c, d, e = R3(a, b, c, d, e, 55)
    e, a, b, c, d = R3(e, a, b, c, d, 56)
    d, e, a, b, c = R3(d, e, a, b, c, 57)
    c, d, e, a, b = R3(c, d, e, a, b, 58)
    b, c, d, e, a = R3(b, c, d, e, a, 59)

    a, b, c, d, e = R4(a, b, c, d, e, 60)
    e, a, b, c, d = R4(e, a, b, c, d, 61)
    d, e, a, b, c = R4(d, e, a, b, c, 62)
    c, d, e, a, b = R4(c, d, e, a, b, 63)
    b, c, d, e, a = R4(b, c, d, e, a, 64)
    a, b, c, d, e = R4(a, b, c, d, e, 65)
    e, a, b, c, d = R4(e, a, b, c, d, 66)
    d, e, a, b, c = R4(d, e, a, b, c, 67)
    c, d, e, a, b = R4(c, d, e, a, b, 68)
    b, c, d, e, a = R4(b, c, d, e, a, 69)
    a, b, c, d, e = R4(a, b, c, d, e, 70)
    e, a, b, c, d = R4(e, a, b, c, d, 71)
    d, e, a, b, c = R4(d, e, a, b, c, 72)
    c, d, e, a, b = R4(c, d, e, a, b, 73)
    b, c, d, e, a = R4(b, c, d, e, a, 74)
    a, b, c, d, e = R4(a, b, c, d, e, 75)
    e, a, b, c, d = R4(e, a, b, c, d, 76)
    d, e, a, b, c = R4(d, e, a, b, c, 77)
    c, d, e, a, b = R4(c, d, e, a, b, 78)
    b, c, d, e, a = R4(b, c, d, e, a, 79)

    H[0] += a
    H[1] += b
    H[2] += c
    H[3] += d
    H[4] += e

    for i in range(len(H)):
        H[i] = H[i] & 0xFFFFFFFF

    return H

def main():
    global H
#    msg = 'abc'
    msg = 'abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq'

    hash = block(H, padding(msg.encode()))

    print(hash)
    print(toStr(hash))
    
if __name__ == '__main__':
    main()
