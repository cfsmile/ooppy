class MySubClass(object):
    pass


class Contact():
    """Contact class with list of entries """

    #  Class variable, because it is part of the class definition, is shared
    # by all instances of this class.
    all_contacts = []

    def __init__(self, name, email):

        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supplier(Contact):
    """Subclass of Contact records contact of suppliers"""
    def order(self, order):
        print("We would send '{}' order to '{}'".format(order, self.name))


if __name__ == "__main__":
    c = Contact("some body", "sb@ex.net")
    s = Supplier("SP", "sp@ex.net")

    print(c.name, c.email, s.name, s.email)
    c.all_contacts
    # c.order("I need pliers")
    # AttributeError: 'Contact' object has no attribute 'order'
    s.order("I need pliers")
