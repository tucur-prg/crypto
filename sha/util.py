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
