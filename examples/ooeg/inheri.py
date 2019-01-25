#+begin_src python :results output
  # 继承语法

  class MySubClass(object):
      pass

  # 例子： 通讯录，比如客户经理留存的客户通讯录，内有姓名和电邮

class Contact:
    """
    通讯录类，以list包含若干通讯记录
    """
    # 类变量
    all_contacts = []  #  Class variable, because it is part of the
                       #  class definition, is shared by all instances
                       #  of this class.

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supplier(Contact):
    """通讯录类的子类，仅记录供应商的联系方式"""
    def order(self, order):
        print("If this were a real system we would send '{}' order to '{}'".format(order, self.name))

if __name__ == "__main__":
    c = Contact("some body", "sb@ex.net")
    s = Supplier("SP", "sp@ex.net")

    print(c.name, c.email, s.name, s.email)
    c.all_contacts
    # c.order("I need pliers")  # AttributeError: 'Contact' object has no attribute 'order'
    s.order("I need pliers")
#+end_src
