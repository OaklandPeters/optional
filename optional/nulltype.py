import abc
import types
import collections



__all__ = ['NullType', 'NotPassed']

class NullType(object):
    """Superclass of NoneType, NotPassed, and optional."""
    __metaclass__ = abc.ABCMeta
NullType.register(types.NoneType)

class NotPassed(NullType):
    pass
