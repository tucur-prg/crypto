from fp import Fp
from fr import Fr

#
# 楕円曲線
# 次の形の方程式により定義される平面曲線
# y^2 = x^3 + ax + b
#
# 楕円曲線暗号に使う楕円曲線の式
# y^2 = x^3 + ax + b mod p
#
# 公開鍵の生成
# 1. 楕円曲線のパラメータであるp,a,b、また基準点であるG(x,y)を決める
# 2. Gに自身であるGを足し、2Gを求める（楕円曲線暗号における足し算）
# 3. 2.の行為をn回分（n：秘密鍵の値）繰り返すことで、値nGを得る
# 4. nGを公開鍵の値とする
#
class Ec:
    # E : y^2 = x^3 + ax + b mod p. r is the order of E
    @classmethod
    def init(cls, a, b, r):
        if type(a) is int:
            a = Fp(a)
        if type(b) is int:
            b = Fp(b)
        cls.a = a # 傾き
        cls.b = b # 切片
        cls.r = r

    def __init__(self, x=None, y=None, doVerify=True):
        self.isZero = True
        if x is None and y is None:
            return
        if type(x) is int:
            x = Fp(x)
        if type(y) is int:
            y = Fp(y)
        self.x = x
        self.y = y
        self.isZero = False
        if doVerify and not self.isValid():
            raise Exception(f"isValid x={x}, y={y}")
    def __str__(self):
        if self.isZero:
            return "O"
        else:
            return f"({self.x}, {self.y})"
    def __eq__(self, rhs):
        if self.isZero:
            return rhs.isZero
        if rhs.isZero:
            return False
        return self.x == rhs.x and self.y == rhs.y

    def isValid(self):
        if self.isZero:
            return True
        return self.y * self.y == (self.x * self.x + self.a) * self.x + self.b

    def __neg__(self):
        if self.isZero:
            return self
        return Ec(self.x, -self.y, False)

    def __add__(self, rhs):
        if self.isZero:
            return rhs
        if rhs.isZero:
            return self
        x1 = self.x
        y1 = self.y
        x2 = rhs.x
        y2 = rhs.y

        # P(x,y) + Q(x,y)
        # 傾き = Yの変化量 / Xの変化量
        # L = (Yq - Yp) / (xq - Xp)

        # 同じ点の加算
        # 1、点Pの接線を引く
        # 2、楕円曲線との交点を求める
        # 3、その交点とx軸に対して、対称な楕円曲線上の点を求める。
        # 4、その点をPの2倍加算である2Pとして定義する

        if x1 == x2:
            # P + (-P) = 0
            if y1 == -y2:
                return Ec()
            # DBL (倍増)
            L = x1 * x1
            L = (L + L + L + self.a) / (y1 + y1)
        else:
            L = (y1 - y2) / (x1 - x2)

        # Xr = L^2 - Xp + Xq
        # Yr = L(Xp - Xr) - Yp

        x3 = L * L - (x1 + x2)
        y3 = L * (x1 - x3) - y1
        return Ec(x3, y3, False)

    def __mul__(self, rhs):
        if type(rhs) is Fr:
            rhs = rhs.v
        elif type(rhs) is not int:
            raise Exception("bad type", rhs)
        if rhs == 0:
            return Ec()
        bs = bin(rhs)[2:]
        ret = Ec()
        for b in bs:
            ret += ret
            if b == '1':
                ret += self
        return ret
