import math
from prime import numbers
from util import decimal_hex_digest

# ハッシュ初期値(Initial Hash Value)
# 素数の小さい順で8個の数を、平方根した少数部分の32bitsの値です。

H = [hex(i)[2:].rjust(8, '0') for i in [
    0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
]]

def main():
    prime = numbers(8)

    _H = list(
        map(
            lambda x: decimal_hex_digest(math.sqrt(x)),
            prime
        )
    )
    
    for i in range(len(H)):
        print(H[i], _H[i], prime[i], H[i] == _H[i])
    
if __name__ == '__main__':
    main()
