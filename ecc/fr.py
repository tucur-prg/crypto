import secrets

# 有限体
class Fr:
    @classmethod
    def init(cls, p):
        cls.p = p

    def setRand(self):
        self.v = secrets.randbelow(self.p)

    def __init__(self, v=0):
        self.v = v % Fr.p

    def __eq__(self, rhs):
        if type(rhs) is int:
            return self.v == rhs
        return self.v == rhs.v

    def __str__(self):
        return hex(self.v)[2:]

    def __neg__(self):
        return Fr(-self.v)

    def __add__(self, rhs):
        return Fr(self.v + rhs.v)

    def __sub__(self, rhs):
        return Fr(self.v - rhs.v)

    def __mul__(self, rhs):
        return Fr(self.v * rhs.v)

    def __truediv__(self, rhs):
        return self * rhs.inv()

    def inv(self):
        # v * v^(p-2) = v^(p-1) = 1 mod p
        if self.v == 0:
            raise Exception("zero inv")
        return Fr(pow(self.v, Fr.p - 2, Fr.p))
