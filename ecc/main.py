from ec import Ec, Fp, Fr
from ecdsa import sign, verify, msgToFr
from curve import prime256v1

def main():
    curve = prime256v1()

    Fp.init(curve.p)
    Fr.init(curve.n)
    Ec.init(curve.a, curve.b, curve.n)

    P = Ec(curve.Gx, curve.Gy)

    priv = Fr(0x13f55dd31a23316169e913542629220878f14efe19da836a8741eb2419f5d554)

    print("PrivateKey")
    print("d: {}".format(priv))
    print("")

    pub = P * priv

    print("PublicKey");
    print("x: {}".format(pub.x))
    print("y: {}".format(pub.y))
    print("")

    msg = b"hello"

    print("hash")
    print(msgToFr(msg))
    print("")

    (r, s) = sign(P, priv, msg)

    print("Signature")
    print("r: {}".format(r))
    print("s: {}".format(s))
    print("compact: {}{}".format(r, s))
    print("")

    assert verify(P, (r, s), pub, msg) == True
    assert verify(P, (r, s), pub, b"x") == False

if __name__ == '__main__':
    main()
