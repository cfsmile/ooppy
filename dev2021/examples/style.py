# -*- encoding: utf-8 -*-
#!/usr/bin/env python


def fibs(num):
    """
    This is a Fibnacci function
    """
    result = [0, 1]
    for i in range(num-2):
        result.append(result[-2] + result[-1])
    return result  # This is a comment
