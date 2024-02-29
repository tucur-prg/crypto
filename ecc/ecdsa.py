from ec import Fr
import hashlib

def byteToFr(b):
    v = 0
    for x in b:
        v = v * 256 + x
    return Fr(v)

def msgToFr(msg):
    H = hashlib.sha256()
    H.update(msg)
    return byteToFr(H.digest())

def sign(P, sec, msg, k=None):
    z = msgToFr(msg)
    if k is None:
        k = Fr()
        k.setRand()
    Q = P * k
    r = Fr(Q.x.v)
    s = (r * sec + z) / k
    return (r, s)

def verify(P, sig, pub, msg):
    (r, s) = sig
    if r == 0 or s == 0:
        return False
    z = msgToFr(msg)
    w = Fr(1) / s
    u1 = z * w
    u2 = r * w
    Q = P * u1 + pub * u2
    if Q.isZero:
        return False
    x = Fr(Q.x.v)
    return r == x
