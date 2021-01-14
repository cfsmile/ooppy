class A:
    def hello(self):
        print("Hello, I'm A")


class B(A):
    # pass
    def hello(self):  # override superclass's hello()
        print("Hello, I'm B")


a = A()
b = B()
a.hello()
b.hello()
