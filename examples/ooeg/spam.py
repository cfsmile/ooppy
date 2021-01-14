# -*- coding: utf-8 -*-
#!/usr/bin/env python


# class Spam(object):
#     '''
#     The Spam object contains lots of spam descripted by Sphinx style.

#     :param arg: The arg is used for ...
#     :type arg: str
#     :param `*args`: The variable arguments are used for ...
#     :param `**kwargs`: The keyword arguments are used for ...
#     :ivar arg: This is where we store arg
#     :vartype arg: str
#     '''
#     def __init__(self, arg, *args, **kwargs):
#         self.arg = arg

#     def eggs(self, amount, cooked):
#         '''We can't have spam without eggs, so here's the eggs

#         :param amount: The amount of eggs to return
#         :type amount: int
#         :param bool cooked: Should the eggs be cooked?
#         :raises: :class:`RuntimeError`: Out of eggs

#         :returns: A bunch of eggs
#         :rtype: Eggs
#         '''
#         pass


class Spam(object):
    '''
    The Spam object contains lots of spam descripted by Google style.

    Args:
        arg (str): The arg is used for ...
        *args: The variable arguments are used for ...
        **kwargs: The keyword arguments are used for ...
        
    Attributes:
        arg (str): This is where we store arg,
    '''
    def __init__(self, arg, *args, **kwargs):
        self.arg = arg

    def eggs(self, amount, cooked):
        '''We can't have spam without eggs, so here's the eggs

        Args:
            amount (int): The amount of eggs to return
            cooked (bool): Should the eggs be cooked?
        
        Raises:
            RuntimeError: Out of eggs
        
        Returns:
            Eggs: A bunch of eggs
        '''
        pass
