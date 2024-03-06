import sys
import random
import hashlib

# -----------
def modular_exp(a, b, n):
    res = 1
    while b != 0:
        if b & 1 != 0:
            res = (res * a) % n
        a = (a * a) % n
        b = b >> 1

    return res

# -----------
def gen_rand(bit_length):
    bits = [random.randint(0,1) for _ in range(bit_length - 2)]
    ret = 1
    for b in bits:
        ret = ret * 2 + int(b)
    return ret * 2 + 1

def mr_primary_test(n, k=100):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = n - 1
    s = 0
    while d % 2 != 0:
        d /= 2
        s += 1

    r = [random.randint(1, n - 1) for _ in range(k)]
    for a in r:
        if modular_exp(a, d, n) != 1:
            pl = [(2 ** rr) * d for rr in range(s)]
            flg = True
            for p in pl:
                if modular_exp(a, p, n) == 1:
                    flg = False
                    break
            if flg:
                return False
    return True

def gen_prime(bit):
    while True:
        ret = gen_rand(bit)
        if mr_primary_test(ret):
            break
    return ret

# -----------
def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0

def gen_d(e, l):
    _, x, _ = xgcd(e, l)
    return x % l

# -----------
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - y * (a // b)

def calculate_private_key(e, phi):
    gcd, x, y = extended_gcd(e, phi)
    # Ensure that the private key exponent (d) is positive
    d = x if x > 0 else x + phi
    
    return d

# -----------
def main(calc):
    bit_size = 2048

    p = 132153101622512491672225059683386684053100994134393383936217500502837561679526938662147742983462313673459000403453485087688588483815174735876261585223049907477880772508718020616780417849058663206917968546843826381124874700257276403481705294152961909223866163954630643365713280098342802040373875810244083496487
    q = 142643524884643353741902710637184179346393281925971417334137554259853243552343829770262608425692971034373769111583335863497220912567267351896376136074792895107167093480782140807312944851005828557299238680449011370860231222058805936799564162238921395786982479508891919413640536248674575662684836688351444762573

    if calc == "1":
        p = gen_prime(bit_size//2)
        q = gen_prime(bit_size//2)
        print("p", p)
        print("q", q)

    #e = gen_prime(bit_size)
    e = 65537
#    d = gen_d(e, (p - 1) * (q - 1))
    d = calculate_private_key(e, (p - 1) * (q - 1))
    n = p * q
    print("e", e)
    print("d", d)
    print("n", n)

    # crypto
    m = 123456789
    c = modular_exp(m, e, n)  # 暗号文
    m_ = modular_exp(c, d, n)  # 123456789    
    print(m)
    print(c)
    print(m_)

    # signature
    msg = "abc"
    hash = hashlib.sha256(msg.encode())
    i = int.from_bytes(hash.digest())
    print("signature")
    print("hex", hex(i)[2:])
    print("int", i)
    sign = modular_exp(i, d, n)
    print(sign)
    print("verify")
    verify = modular_exp(sign, e, n)
    print("hex", hex(verify)[2:])
    print("int", verify)

    print("signature")
    print("hex", hash.hexdigest())
    sign = [modular_exp(ord(_char), d, n) for _char in hash.hexdigest()]
    print("verify")
    verify = [chr(modular_exp(_byte, e, n)) for _byte in sign]
    print("hex", "".join(verify))


if __name__ == '__main__':
    calc = ""
    if len(sys.argv) > 1:
        calc = sys.argv[1]
    main(calc)
