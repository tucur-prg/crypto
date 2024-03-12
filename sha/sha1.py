import hashlib

from logical import ch_, maj_, parity
from bit import rotl32
from util import padding, toStr

K = [
    0x5a827999, 0x6ed9eba1, 0x8f1bbcdc, 0xca62c1d6
]

_H = [
    0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0
]

def compute(msg):
    N = len(msg) // 64

    W = list(range(80))
    H = list(range(len(_H)))
    for i in range(len(_H)):
        H[i] = _H[i]

    for i in range(1, N+1):
        for t in range(80):
            if t < 16:
                p = (i - 1) * 64 + t * 4
                W[t] = (msg[p] << 24) + (msg[p + 1] << 16) + (msg[p + 2] << 8) + msg[p + 3]
            else:
                W[t] = rotl32(W[t-3] ^ W[t-8] ^ W[t-14] ^ W[t-16], 1)

        a, b, c, d, e = H

        for t in range(80):
            if t <= 19:
                f = ch_
            elif t <= 39:
                f = parity
            elif t <= 59:
                f = maj_
            else:
                f = parity

            T = (rotl32(a, 5) + f(b, c, d) + e + W[t] + K[t // 20])&0xFFFFFFFF
            e = d
            d = c
            c = rotl32(b, 30)
            b = a
            a = T

        H[0] = (a + H[0]) & 0xFFFFFFFF
        H[1] = (b + H[1]) & 0xFFFFFFFF
        H[2] = (c + H[2]) & 0xFFFFFFFF
        H[3] = (d + H[3]) & 0xFFFFFFFF
        H[4] = (e + H[4]) & 0xFFFFFFFF

    return H

MASK = 0x0000000F
def compute2(msg):
    N = len(msg) // 64

    W = list(range(80))
    H = list(range(len(_H)))
    for i in range(len(_H)):
        H[i] = _H[i]

    for i in range(1, N+1):
        for t in range(80):
            if t < 16:
                p = (i - 1) * 64 + t * 4
                W[t] = int.from_bytes(msg[p:p+4], 'big')

        a, b, c, d, e = H

        for t in range(80):
            s = t & MASK
            if t >= 16:
                W[s] = rotl32(W[(s+13)&MASK]  ^ W[(s+8)&MASK] ^ (W[(s+2)&MASK]) ^ (W[s]), 1) & 0xffffffff

            if t <= 19:
                f = ch_
            elif t <= 39:
                f = parity
            elif t <= 59:
                f = maj_
            else:
                f = parity

            T = (rotl32(a, 5) + f(b, c, d) + e + W[s] + K[t // 20]) &0xFFFFFFFF
            e = d
            d = c
            c = rotl32(b, 30)
            b = a
            a = T

        H[0] = (a + H[0]) & 0xFFFFFFFF
        H[1] = (b + H[1]) & 0xFFFFFFFF
        H[2] = (c + H[2]) & 0xFFFFFFFF
        H[3] = (d + H[3]) & 0xFFFFFFFF
        H[4] = (e + H[4]) & 0xFFFFFFFF

    return H

def main():
    #import binascii
    #bs = binascii.hexlify(padding(b"\x61\x62\x63\x64\x65"))
    #print([bs[i*8:i*8+8] for i in range(len(bs) // 8)])

    msg = 'abc' # a9993e36 4706816a ba3e2571 7850c26c 9cd0d89d
    msg = 'abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq' # 84983e44 1c3bd26e baae4aa1 f95129e5 e54670f1
    #msg = 'a' * 1000000 # 34aa973c d4c4daa4 f61eeb2b dbad2731 6534016f

    pad_msg = padding(msg.encode())

    hash = compute(pad_msg)
    print(hash)
    print(toStr(hash))

    hash = compute2(pad_msg)
    print(hash)
    print(toStr(hash))

    print(hashlib.sha1(msg.encode()).hexdigest())
    
def tb(b):
    return bin(b)[2:].rjust(8, '0')

if __name__ == '__main__':
    main()
