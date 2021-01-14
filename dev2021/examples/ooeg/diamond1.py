class A:
    def ping(self):
        print('ping:', self)


class B(A):
    def pong(self):
        print('B-pong', self)


class C(A):
    def pong(self):
        print('C-PONG:', self)


class D(B, C):  # Try class D(C, B): , see what happens

    def ping(self):
        super().ping()
        print('post-ping', self)

    def pingpong(self):
        self.ping()
        super.ping()
        self.pong()
        super.pong()
        C.pong(self)


d = D()
d.pong()  # version B
C.pong(d)
D.__mro__

d.pingpong()


def print_mro(cls):
    print(', '.join(c.__name__ for c in cls.__mro__))


print_mro(D)
