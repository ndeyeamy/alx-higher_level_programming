#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """ Return the integer addition of a and b
    must be integers or floats, otherwise raise a
    TypeError exception with the message a must be
    an integer or b must be an integer
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    return (int(a) + int(b))
