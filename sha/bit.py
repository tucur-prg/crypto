
def rotl(x, n, w = 32):
    return (x << n) | (x >> (w - n))

def rotr(x, n, w = 32):
    return (x >> n) | (x << (w - n))

def shr(x, n):
    return x >> n

def rotl32(x, n):
    return ((x << n) | (x >> (32 - n))) & 0xffffffff
    
def rotr32(x, n):
    return ((x >> n) | (x << (32 - n))) & 0xffffffff
