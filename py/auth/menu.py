#! /usr/bin/env python
# -*- encoding:utf-8 -*-


import auth


# Set up a test user and permission

# joe can login as a user.
auth.authenticator.add_user("joe", "joepassword")

## there are two oprations that a authorized user can perform.
auth.authorizor.add_permission("test program")
auth.authorizor.add_permission("change program")

## joe is authorized with the 'test program' ops. He CAN test program.
auth.authorizor.permit_user("test program", "joe")

## joe is unauthorized with the 'change program' ops. He CANNOT change program.
## If the next statement is uncomment, joe surely CAN 'change program'.

# auth.authorizor.permit_user("change program", "joe")


class Editor:
    """"""
    def __init__(self):
        """"""
        self.username = None
        self.menu_map = {
            "login": self.login,
            "test": self.test,
            "change": self.change,
            "quit": self.quit
        }

    def login(self):
        """"""
        logged_in = False
        while not logged_in:
            username = input("username: ")
            password = input("password: ")
            try:
                logged_in = auth.authenticator.login(username, password)
                # TODO: add a count var to record trying login times.If
                # trying more than 3 times, break the loop.
            except auth.InvalidUsername:
                print("Sorry, that username does not exist")
            except auth.InvalidPassword:
                print("Sorry, incorrect password")
            else:
                self.username = username

    def is_permitted(self, permission):
        """"""
        # print("permission is {}".format(permission))
        # print("self.username is {}".format(self.username))
        # print("{}".format(auth.authorizor.authenticator.is_logged_in(self.username)))
        try:
            auth.authorizor.check_permission(permission, self.username)
        except auth.NotLoggedInError as e:
#            print("{0} is not logged in".format(e.username))
            return False
        except auth.NotPermittedError as e:
            print("{0} cannot {1}".format(e.username, permission))
            return False
        else:
            return True

    def test(self):
        """"""
        if self.is_permitted("test program"):
            print("Testing program now...")

    def change(self):
        """"""
        if self.is_permitted("change program"):
            print("Changing program now...")

    def quit(self):
        """"""
        raise SystemExit()

    def menu(self):
        """"""
        try:
            answer = ""
            while True:
                print("""
                Please enter a command:
                \tlogin\tLogin
                \ttest\tTest the program
                \tchange\tChange the program
                \tquit\tQuit
                """)
                answer = input("enter a command: ").lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print("{0} is not a valid option".format(answer))
                else:
                    func()
        finally:
            print("Thank you for testing the auth module")


Editor().menu()

####
# login, test,quit func do work. change fucntion does not work, which raises
# an exception:
# enter a command: change
# joe is not logged in

#                 Please enter a command:
#                       login	Login
#                       test	Test the program
#                       change	Change the program
#                       quit	Quit

# enter a command: test
# Testing program now...

#                 Please enter a command:
#                       login	Login
#                       test	Test the program
#                       change	Change the program
#                       quit	Quit

# enter a command: login
