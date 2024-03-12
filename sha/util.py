def decimal_hex_digest(num):
    h = 2 ** 4
    u = 1 / h
    s = ""
    num %= 1
    for i in range(8):
        d = num // u
        s += hex(int(d))[2:]
        num = (num - u  * d)
        num *= h
    return s

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

def toStr(hash):
    return ''.join([hex(i)[2:].rjust(8, '0') for i in hash])
