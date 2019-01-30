class AddressHolder:
    def __int__(self, street, city, state, code):

        self.street = street
        self.city = city
        self.state = state
        self.code = code


class Friend(Contact, AddressHolder):
    def __init__(self,
                 name,
                 email,
                 phone,
                 street,
                 city,
                 state,
                 code):

        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, city, state, code)
        self.phone = phone
