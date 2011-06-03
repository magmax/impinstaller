#!/usr/bin/python
# -*- coding:utf-8; tab-width:4; mode:python -*-

# Taken from pyarco

"""
moduleauthor:: Arco Research Group
"""

import threading

class Singleton(type):

    """A metaclass for make any other class a Singleton_ (the design pattern).
    Example of use::

    class MySingletonClass:
        __metaclass__ = Singleton
        # your code goes here :)

    .. _Singleton: http://en.wikipedia.org/wiki/Singleton_pattern
    """
    def __init__(cls, name, bases, dct):
        cls.__lock = threading.Lock()
        cls.__instance = None
        type.__init__(cls, name, bases, dct)

    def __call__(cls, *args, **kw):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = type.__call__(cls, *args, **kw)
        return cls.__instance

    def loaded(cls):
        return cls.__instance != None
