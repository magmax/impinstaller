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


class TypedAttr(object):
    """
    Taken from http://crysol.org/es/node/1500
    """

    def __init__(self, name, cls):
        self.name = name
        self.cls = cls

    def __get__(self, obj, objtype):
        if (obj is None):
            raise AttributeError

        try:
            return obj.__dict__[self.name]
        except KeyError:
            raise AttributeError

    def __set__(self, obj, val):
        if not isinstance(val, self.cls):
            raise TypeError("'%s' given but '%s' expected" % (val.__class__.__name__, self.cls.__name__))

        obj.__dict__[self.name] = val
