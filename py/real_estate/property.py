#! /usr/env/bin python
# -*- coding: utf-8 -*-

class Property:
    """
    """
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        # **kwargs is prepared for a multiple inheritance situation.
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        return dict(square_feet = input("Enter the square feet: "),
                    beds = input("Enter number of bedrooms: "),
                    baths = input("Enter number of baths: "))

    prompt_init = staticmethod(prompt_init)
    #  Static mehtods are associated only with a class (something like class variables),
    #  rather than a specific object instance. Hense, they have no self argument.
    #  Because of this, super won't work(there is no parent object,only a parent class),
    #  so we simply call the staticmethod on the parent class directly.

class Apartment(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarim")

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    def prompt_init():
        #  so we simply call the staticmethod on the parent class directly.
        parent_init = Property.prompt_init()

        laundry = ''
        while laundry.lower() not in Apartment.valid_laundries:
            laundry = input("What laundry facilities does the property have? ({})".format(", ".join(Apartment.valid_laundries)))

        balcony = ''
        while balcony.lower() not in Apartment.valid_balconies:
            balcony = input("Does the property have a balcony? ({})".format(", ".join(Apartment.valid_balconies)))
        # dict.update to merge the new dictionary values into the first one.
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init
    # ver 2, use module-level function to erase duplicate code
    # This is much easier to read (and maintain!) than original version.
#     def prompt_init():
#         #  so we simply call the staticmethod on the parent class directly.
#         parent_init = Property.prompt_init()

#         laundry = get_valid_input("What laundry facilities does the property have? ",
#                                   Apartment.valid_laundries)

#         balcony = get_valid_input("Does the property have a balcony? ",
#                                   Apartment.valid_balconies)
#         # dict.update to merge the new dictionary values into the first one.
#         parent_init.update({
#             "laundry": laundry,
#             "balcony": balcony
#         })
#         return parent_init

    prompt_init = staticmethod(prompt_init)

# Improve duplicate code with module-level function

def get_valid_input(input_string, valid_options):
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response

class House(Property):
    valid_garage = ("attatched", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        super().display()
        print("HOUSE DETAILS")
        print("# of sotries: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ", House.valid_fenced)
        garage = get_valid_input("Is there a garage? ", House.valid_garage)
        num_stories = input("How many sotries? ")

        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)

class Purchase:
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        return dict(price=input("What is the selling price?"),
                   taxes=input("What are the estimated taxes?"))

    prompt_init = staticmethod(prompt_init)


class Rental:
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        return dict(rent=input("What is the monthly rent? "),
                   utilities=input("What are the estimated utilities? "),
                   furnished=get_valid_input("Is the property furnished? ", ("yes", "no")))

    prompt_init = staticmethod(prompt_init)

#  These two classes don't have a superclass (other than object), but we still call super().__init__, because
#  they are going to be combined with other classes, and we don't know what order the super calls will be made in.

class HouseRental(Rental, House):
    def prompt_init():
        """
        docstring.

        This is surprising, as the class on its own has neither an __init__ nor
        display method! Because both parent classes appropriately call super in these
        method, we only have to extend those classes and the classes will behave in the
        correct order.

        This is not the case with promtp_init, since it is a static method that does not
        call super, so we implement this one explicitly."""
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

# The prompt_init method is promptint for initializers to all the super classes, and display()
# is also cooperatively calling all three superclasses.

#  test
#  init = HouseRental.prompt_init()
#  house = HouseRental(**init)
#  house.display()

class ApartmentRental(Rental, Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)

class ApartmentPurchase(Purchase, Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)

class HousePurchase(Purchase, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)

# Above should be the most intense designing out of our way!

# Now, create the Agent class responsible for creating new listings
# and displaying existing ones.

class Agent:
    # this is class variable and it is a dictionary, where the keys are
    # tuples of two distinct strings,and the values are class objects.

    #  Classes can be passed around, renamed, and stored in containers just
    #  like normal object or primitive data types.
    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "purchase"): ApartmentPurchase,
        ("apartment", "rental"): ApartmentRental
    }

    def __init__(self):
        self.property_list = []

    def display_properties(self):
        for property in self.property_list:
            property.display()

    def add_property(self):
        property_type = get_valid_input("What type of property? ", ("house", "apartment")).lower()
        payment_type = get_valid_input("What payment type? ", ("purchase", "rental")).lower()

        #  This is dictionary selection, getting one of the four type_map values,
        #  which are classNames.
        PropertyClass = self.type_map[(property_type, payment_type)]


        init_args = PropertyClass.prompt_init() # get init, which is dictionary
        self.property_list.append(PropertyClass(**init_args))


# test

if __name__ == "__main__":
    agent = Agent()
    agent.add_property()
    agent.add_property()
    agent.display_properties()
