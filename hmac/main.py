import hashlib
import binascii

def sha256(message):
    return hashlib.sha256(message).digest()
 
def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])
 
block = b"\x00"
ipad = b"\x36" * 64
opad = b"\x5c" * 64

def main():
    secret = 0xad4c96714d2a6289ed1731742ecfb1959430469ab30d7b2c4c212124153c23bf

    message = b"hello world"
    
    l = secret.bit_length() // 8
    key = secret.to_bytes(l)
    
    key = b'0123456789' * 6 + b'0123'

    print(key)
    print(binascii.hexlify(key))

    # key convert
    if len(key) > 64:
        key = sha256(key)

    if len(key) < 64:
        key = key + block * (64 - len(key))

    print(key)
    print(binascii.hexlify(key))

    # salt
    i = xor(ipad, key)
    o = xor(opad, key)
    
    # signature
    signature = sha256(o + sha256(i + message))
    
    print(signature)
    print(binascii.hexlify(signature))

    # 55e10fb7424b66cf001f4a81d21c4ff9ce8b051463e3ef3cf43449c0383aef6d

if __name__ == '__main__':
    main()
