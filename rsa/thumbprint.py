import hashlib
import base64

# pub > pem
# ssh-keygen -f test_rsa.pub -e -m pem

# pem > pub
# ssh-keygen -i -f filename

def main():
    # ssh-keygen -lf id_rsa.pub

    pubkey = "AAAAB3NzaC1yc2EAAAADAQABAAABgQCwvZQuaBGtoGng+6XmL1ICvlG6nZGgfRebdKtVT3a/YEtiZ3r7MKqV8L/go18RZinEDEU9ogwJhlS7egR1MJF7s6RQRELP1drX2q7Mvw8EvDaHhtkAg5VG2suwDa9GvcpzVmWY3pTiBcOkVtGlNxz8t8zBp5265byUX6p/PVoPNJP6DIKLhQ0lBmUptJdnvhklVET7fMVuAIvaOn9YkLUHlxa0QQAG1LEMEsG7hBEtZKQEvVjosPkx63tIDklu6H0KNWurb1I3Ee6aUinEmp6qMw9K/oUQemCIniRBr99gTPZHO1JYKktskmNY8yZvjU3waigPwAptEMLOletghjGMQPUxBreWhK4jbX9ta6DSuSxDcU+wQjpa3vdEZ3fQIb7TcTwhHacKXjVpNMLz+y0eUDCESAhHizGmRGRWuYTUMD9oUGm8iSP6JSIhrr3p9KgTwyfopD5JO+FVil746pHyRq+xVNnyY2CZLMX0581qyNovAdbTSDqy+nqtbrZVSNs="

    raw = base64.b64decode(pubkey.encode())
    print(raw)

    hash = hashlib.sha256(raw)
    i = int.from_bytes(hash.digest())

    print('')
    print(hex(i)[2:])
    print("thumbprint: SHA256: {}".format(base64.b64encode(hash.digest()).rstrip(b'=').decode()))

if __name__ == '__main__':
    main()
