class curve:
    def __init__(self, a, b, p, r, Gx, Gy):
        self.a = a
        self.b = b
        self.p = p
        self.r = r
        self.Gx = Gx
        self.Gy = Gy

def secp256k1():
    return curve(**{
        "a": 0x0000000000000000000000000000000000000000000000000000000000000000,
        "b": 0x0000000000000000000000000000000000000000000000000000000000000007,
        "p": 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f,
        "r": 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141,
        "Gx": 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
        "Gy": 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8,
    })

def prime256v1():
    return curve(**{
        "a": 0xffffffff00000001000000000000000000000000fffffffffffffffffffffffc,
        "b": 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b,
        "p": 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff,
        "r": 0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551,
        "Gx": 0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296,
        "Gy": 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5,
    })
