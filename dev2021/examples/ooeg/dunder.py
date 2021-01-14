# coding: utf-8
#!/usr/bin/env python


class A():
    """Example for information hiding"""

    def __init__(self):

        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"


x = A()

x.pub
x.pub = x.pub + " and my value can be changed"
x.pub

x._prot
x.__priv
