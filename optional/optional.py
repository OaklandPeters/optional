"""



@todo: Change Optional() and deoption() to use NotPassed
@todo: Look at bugs/unit-testing dealing with user importing NullType from another source
    --> getting NoneType to respect that?
@todo: Look at examples from:
        Lingospot
        fn.py
        Haskell
        Rust
"""
from __future__ import absolute_import
import collections
from .nulltype import NullType, NotPassed, NotPassedType, Optionable

__all__ = ['Optional', 'deoption', 'DeoptionError']



#class Optional(NullType):
#class Optional(Optionable):
class Optional(NotPassedType):
    """Simple implementation of an 'Optional' data type.
    An alternative to passing around 'None', in cases where 'None' might be
    normally be passed in for that parameter. Closely related to 'NotPassed'.
    """
    def __init__(self, default=NotPassed, execute=NotPassed):
        self.default, self.execute = self._validate(default, execute)

    def _validate(self, default=NotPassed, execute=NotPassed):
        if not isinstance(execute, (NotPassedType, collections.Callable)):
            raise TypeError("'execute' must be NotPassed or Callable.")
        if isinstance(default, NotPassedType) and isinstance(execute, NotPassedType):
            raise TypeError("At least one argument must be provided: "
                "'execute' or 'default'.")
        return default, execute

    def deoption(self):
        return deoption(None, self.default, self.execute)
        
    @property
    def value(self):
        return self.deoption()

    def __repr__(self):
        return "Optional({0})".format(self._deoption_repr())
    def _deoption_repr(self):
        if not isinstance(self.execute, NotPassedType):
            return repr(self.execute)
        elif not isinstance(self.default, NotPassedType):
            return repr(self.default)
        else:
            raise DeoptionError()


def deoption(obj, default=NotPassed, execute=NotPassed):
    """Used as an 'default' function - to unwrap arguments.
    def myfunction(first=None):
        first = deoption(first, execute=dict)
    """
    # Dispatch: obj provides its own 'deoption' - use that
    if isinstance(obj, Optionable):
        return obj.deoption()
    # obj is valid - return it
    elif not isinstance(obj, NullType):
        return obj
    # execute function was provided - call and return it
    elif not isinstance(execute, NotPassedType):
        # can error if a non-callable 'execute' is passed
        return execute()
    # default value was provided - return it
    elif not isinstance(default, NotPassedType):
        return default
    # error state
    else:
        raise DeoptionError()

class DeoptionError(TypeError):
    _defaultmsg = "Cannot deoption: neither 'default' or 'execute' were provided."
    def __init__(self, message=_defaultmsg):
        super(DeoptionError, self).__init__(message)
        