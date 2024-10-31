import hashlib
import base64

# pub > pem
# ssh-keygen -f test_rsa.pub -e -m pem

# pem > pub
# ssh-keygen -i -f filename

def main():
    # ssh-keygen -lf id_rsa.pub

    pubkey = "AAAAB3NzaC1yc2EAAAADAQABAAABgQCwvZQuaBGtoGng+6XmL1ICvlG6nZGgfRebdKtVT3a/YEtiZ3r7MKqV8L/go18RZinEDEU9ogwJhlS7egR1MJF7s6RQRELP1drX2q7Mvw8EvDaHhtkAg5VG2suwDa9GvcpzVmWY3pTiBcOkVtGlNxz8t8zBp5265byUX6p/PVoPNJP6DIKLhQ0lBmUptJdnvhklVET7fMVuAIvaOn9YkLUHlxa0QQAG1LEMEsG7hBEtZKQEvVjosPkx63tIDklu6H0KNWurb1I3Ee6aUinEmp6qMw9K/oUQemCIniRBr99gTPZHO1JYKktskmNY8yZvjU3waigPwAptEMLOletghjGMQPUxBreWhK4jbX9ta6DSuSxDcU+wQjpa3vdEZ3fQIb7TcTwhHacKXjVpNMLz+y0eUDCESAhHizGmRGRWuYTUMD9oUGm8iSP6JSIhrr3p9KgTwyfopD5JO+FVil746pHyRq+xVNnyY2CZLMX0581qyNovAdbTSDqy+nqtbrZVSNs="

    # https://docs.github.com/ja/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints
    pubkey = "AAAAB3NzaC1yc2EAAAADAQABAAABgQCj7ndNxQowgcQnjshcLrqPEiiphnt+VTTvDP6mHBL9j1aNUkY4Ue1gvwnGLVlOhGeYrnZaMgRK6+PKCUXaDbC7qtbW8gIkhL7aGCsOr/C56SJMy/BCZfxd1nWzAOxSDPgVsmerOBYfNqltV9/hWCqBywINIR+5dIg6JTJ72pcEpEjcYgXkE2YEFXV1JHnsKgbLWNlhScqb2UmyRkQyytRLtL+38TGxkxCflmO+5Z8CSSNY7GidjMIZ7Q4zMjA2n1nGrlTDkzwDCsw+wqFPGQA179cnfGWOWRVruj16z6XyvxvjJwbz0wQZ75XK5tKSb7FNyeIEs4TT4jk+S4dhPeAUC5y+bDYirYgM4GC7uEnztnZyaVWQ7B381AK4Qdrwt51ZqExKbQpTUNn+EjqoTwvqNj4kqx5QUCI0ThS/YkOxJCXmPUWZbhjpCg56i+2aB6CmK2JGhn57K5mj0MNdBXA4/WnwH6XoPWJzK5Nyu2zB3nAZp+S5hpQs+p1vN1/wsjk="

    raw = base64.b64decode(pubkey.encode())
    print(raw)

    hash = hashlib.sha256(raw)
    i = int.from_bytes(hash.digest())

    print('')
    print(hex(i)[2:])
    print("thumbprint: SHA256: {}".format(base64.b64encode(hash.digest()).rstrip(b'=').decode()))

if __name__ == '__main__':
    main()
