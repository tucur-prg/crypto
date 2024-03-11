import hashlib

from logical import ch, maj, sum0, sum1, sigma0, sigma1
from bit import rotr, shr

_K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
];

_H = [
    0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
]

SEPARATOR = b"\x80"
ZERO = b"\x00"

def padding(msg):
    l = len(msg)
    tmp = [ZERO] * 64
    tmp[0] = SEPARATOR
    if l % 64 < 56:
        block = tmp[0:56 - l % 64]
    else:
        block = tmp[0:64 + 56 - l % 64]
    bs = msg + b"".join(block)
    bits = l * 8
    size = [ZERO] * 8
    size[4] = ((bits & 0xff000000) >> 24).to_bytes()
    size[5] = ((bits & 0x00ff0000) >> 16).to_bytes()
    size[6] = ((bits & 0x0000ff00) >> 8).to_bytes()
    size[7] = ((bits & 0x000000ff)).to_bytes()
    bs += b''.join(size)
    return bs

def compute(msg):
    N = len(msg) // 64

    W = list(range(64))
    H = list(range(len(_H)))
    for i in range(len(_H)):
        H[i] = _H[i]

    for i in range(1, N+1):
        for t in range(64):
            if t < 16:
                p = (i - 1) * 64 + t * 4
                W[t] = (msg[p] << 24) + (msg[p + 1] << 16) + (msg[p + 2] << 8) + msg[p + 3]
            else:
                W[t] = (sigma1(W[t - 2]) + W[t - 7] + sigma0(W[t - 15]) + W[t - 16]) & 0xffffffff

        a, b, c, d, e, f, g, h = H

        for t in range(64):
            T1 = (h + sum1(e) + ch(e, f, g) + _K[t] + W[t]) & 0xffffffff
            T2 = (sum0(a) + maj(a, b, c)) & 0xffffffff
            h = g
            g = f
            f = e
            e = (d + T1) & 0xffffffff
            d = c
            c = b
            b = a
            a = (T1 + T2) & 0xffffffff

        H[0] = (a + H[0]) & 0xffffffff
        H[1] = (b + H[1]) & 0xffffffff
        H[2] = (c + H[2]) & 0xffffffff
        H[3] = (d + H[3]) & 0xffffffff
        H[4] = (e + H[4]) & 0xffffffff
        H[5] = (f + H[5]) & 0xffffffff
        H[6] = (g + H[6]) & 0xffffffff
        H[7] = (h + H[7]) & 0xffffffff

    return H

def toStr(hash):
    return ''.join([hex(i)[2:].rjust(8, '0') for i in hash])

def main():
    msg = 'hello world'
    hash = compute(padding(msg.encode()))
    print(toStr(hash))

    print(hashlib.sha256(msg.encode()).hexdigest())

    
if __name__ == '__main__':
    main()
