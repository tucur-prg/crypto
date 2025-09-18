import base64

def key(path):
    with open(path) as f:
        s = ''.join(f.read().strip().split('\n')[1:-1])
        b = base64.b64decode(s)
        l = list(b)
            
        hl = list(map(lambda v: hex(v)[2:].rjust(2, '0'), l))

    return hl;

def main():
    hl = key('server.key')
    print("=== private key ===")
    print(''.join(hl))

    hl = key('server.csr')
    print("=== Signing Request ===")
    print(''.join(hl))

    hl = key('server.crt')
    print("=== Certification ===")
    print(''.join(hl))
    
if __name__ == '__main__':
    main()
