#! /usr/bin/env python
# -*- encoding:utf-8 -*-


import hashlib


# exceptions and errors inheritance hierarchy
class AuthException(Exception):
    """We'll also be defining several exceptions as we go along. We'll start
    with a special `AuthException` base class that accepts a `username` and
    optional `user` object as parameters; most of our self-defined exceptions
    will inherit from this one.
    This second parameter should be an instance of the `User` class associated
    with that `username`."""
    def __init__(self, username, user=None):
        """"""
        super().__init__(username, user)
        self.username = username
        self.user = user


class UsernameAlreadyExists(AuthException):
    """"""
    pass


class PasswordTooShort(AuthException):
    """"""
    pass


class InvalidUsername(AuthException):
    """"""
    pass


class InvalidPassword(AuthException):
    """"""
    pass


class PermissionError(AuthException):
    """"""
    pass


class NotLoggedInError(AuthException):
    """"""
    pass


class NotPermittedError(AuthException):
    """"""
    pass


# Domain classes
class User:
    """a `User` class that stores the `username` and an encrypted `password`.
    """
    def __init__(self, username, password):
        """Create a new user object. The passord will be encrypted before
        stroing."""
        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False

    def _encrypt_pw(self, password):
        """Encrypt the password with the username and return the sha digest.

        Since the code for encrypting a password is required in both `__init__`
        and `check_password`, we pull it out to its own method.
        This way, it only needs to be changed in one place if someone realizes
        it is insecure and needs imporvement.
        """
        hash_string = (self.username + password)
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        """Return True if the password is valid for this user,
        False otherwise."""
        encrypted = self._encrypt_pw(password)
        return encrypted == self.password


class Authenticator:
    """It can simply be a mapping of `username`s to `user` objects, so we'll
    start with a dictionary in the initialization function.

    The method for adding a user needs to check the two conditions(`password`
    length and previously existing `user`s) before creating a new `User`
    instance and adding it to the dictionary """
    def __init__(self):
        """Construct an authenticator to manage users logging in and out.

        ps: __init__ is not a constructor function. __new__ is the constructor
        function. __init__ is the initialization function
        """
        self.users = {}

    def add_user(self, username, password):
        """"""
        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) < 6:
            raise PasswordTooShort(username)

        self.users[username] = User(username, password)

    def login(self, username, password):
        """"""
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)

        if not user.check_password(password):
            raise InvalidPassword(username, user)

        user.is_logged_in = True
        return True

    def is_logged_in(self, username):
        """"""
        if username in self.users:
            return self.users[username].is_logged_in
        return False


class Authorizor:
    """"""
    def __init__(self, authenticator):
        """"""
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self, perm_name):
        """Create a new permission that users can be added to"""
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set()
        else:
            raise PermissionError("Permission Exists")

    def permit_user(self, perm_name, username):
        """Grant the given permission to the user"""
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)

    def check_permission(self, perm_name, username):
        """"""
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True


authenticator = Authenticator()
authorizor = Authorizor(authenticator)


# main function
# def main():
#     """"""
#     authenticator = Authenticator()
#     authorizor = Authorizor(authenticator)


# if __name__ == "__main__":
#     main()


##### test shell command
#####
# Python 3.5.2 (default, Nov 17 2016, 17:05:23)
# [GCC 5.4.0 20160609] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import auth
# >>> authenticator = auth.Authenticator()
# >>> authorizor = auth.Authorizor(authenticator)
# >>> authenticator.add_user("joe", "joepassword")
# >>> authorizor.add_permission("paint")
# >>> authorizor.check_permission("paint", "joe")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/home/fred/Projcect/projects/venv_dir/blackjack/auth/auth.py", line 162, in check_permission
#     raise NotLoggedInError(username)
# auth.NotLoggedInError: ('joe', None)
# >>> authenticator.is_logged_in("joe")
# False
# >>> authenticator.login("joe", "joepassword")
# True
# >>> authorizor.check_permission("paint", "joe")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/home/fred/Projcect/projects/venv_dir/blackjack/auth/auth.py", line 169, in check_permission
#     raise NotLoggedInError(username)
# auth.NotLoggedInError: ('joe', None)
# >>> authenticator.is_logged_in("joe")
# True
# >>> authorizor.check_permission("paint", "joe")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/home/fred/Projcect/projects/venv_dir/blackjack/auth/auth.py", line 169, in check_permission
#     raise NotLoggedInError(username)
# auth.NotLoggedInError: ('joe', None)
# >>> authorizor.check_permission("mix", "joe")
# Traceback (most recent call last):
#   File "/home/fred/Projcect/projects/venv_dir/blackjack/auth/auth.py", line 164, in check_permission
#     perm_set = self.permissions[perm_name]
# KeyError: 'mix'

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/home/fred/Projcect/projects/venv_dir/blackjack/auth/auth.py", line 166, in check_permission
#     raise PermissionError("Permission does not exist")
# auth.PermissionError: ('Permission does not exist', None)
# >>> authorizor.permit_user("mix", "joe")
# Traceback (most recent call last):
#   File "/home/fred/Projcect/projects/venv_dir/blackjack/auth/auth.py", line 151, in permit_user
#     perm_set = self.permissions[perm_name]
# KeyError: 'mix'

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/home/fred/Projcect/projects/venv_dir/blackjack/auth/auth.py", line 153, in permit_user
#     raise PermissionError("Permission does not exist")
# auth.PermissionError: ('Permission does not exist', None)
# >>> authorizor.permit_user("paint", "joe")
# >>> authorizor.check_permission("paint", "joe")
