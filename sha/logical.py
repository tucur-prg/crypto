from bit import rotr, shr

def ch(x, y, z):
    return (x & y) ^ (~x & z)

# w,x,y => ((w&(x^y))^y)
def ch_(x, y, z):
    return (x & y) | (~x & z)
#    return ((x&(y^z))^z)
#    return z ^ (x & (y ^ z))

def maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)

# w,x,y => (((w|x)&y)|(w&x))
def maj_(x, y, z):
    return (x & y) | (x & z) | (y & z)
#    return (((x|y)&z)|(x&y))
#    return (x & y) + (z & (x & y))

def parity(x, y, z):
    return x ^ y ^ z

def sum0(x):
    return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)

def sum1(x):
    return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)

def sigma0(x):
    return rotr(x, 7) ^ rotr(x, 18) ^ shr(x, 3)

def sigma1(x):
    return rotr(x, 17) ^ rotr(x, 19) ^ shr(x, 10)
