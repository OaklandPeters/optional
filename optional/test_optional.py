from __future__ import absolute_import
import unittest
import types

if __name__ == "__main__":
    from optional import * #imports from package, not sub-module
else:
    from .optional import *
    from .nulltype import *

class TestNullType(unittest.TestCase):
    def test_supertype(self):
        self.assert_(isinstance(None, NullType))
        self.assert_(isinstance(Optional('a'), NullType))
        self.assert_(isinstance(NotPassed, NotPassedType))
        self.assert_(isinstance(NotPassed, NullType))
        
        self.assert_(issubclass(type(None), NullType))
        self.assert_(issubclass(types.NoneType, NullType))
        self.assert_(issubclass(Optional, NullType))
        self.assert_(issubclass(NotPassedType, NullType))



class TestOptional(unittest.TestCase):
    def setUp(self):
        def myfunc(first, second=None, third=Optional(5), fourth=Optional(execute=list)):
            #Equivalent: second = deoption(second, 5)
            if isinstance(second, type(None)):
                second = 5
            
            third = deoption(third, 5)
            fourth = deoption(fourth)
            
            return first, second, third, fourth
        self.myfunc = myfunc
        self.expected = ('a', 5, 5, [])
        
        self.ident = lambda: None

    def _option_suite(self, value):
        opt = Optional(value)
        self.assert_(isinstance(opt, Optional))
        self.assert_(isinstance(deoption(opt), type(value)))
        self.assertEqual(deoption(opt), value)

    def test_optional(self):
        self._option_suite('a')
        self._option_suite(5)
        
        value = None
        self._option_suite(value)
        self.assertEqual(deoption(value, 'a'), 'a')
        
        self._option_suite(dict)
        
        self._option_suite(self.ident)
        
    def test_execute(self):
        opt = Optional(None, execute=dict)
        self.assertEqual(deoption(opt), {})
        self.assertEqual(deoption(opt, execute=dict), {})
        self.assertEqual(deoption(None, execute=dict), {})



    def test_optional_arguments(self):
        self.assertEqual(self.myfunc('a'), self.expected)
        self.assertEqual(self.myfunc('a', 5), self.expected)
        self.assertEqual(self.myfunc('a', second=5), self.expected)
        self.assertEqual(self.myfunc('a', 5, 5), self.expected)
        self.assertEqual(self.myfunc('a', fourth=[]), self.expected)
    
    def test_edges(self):
        self.assertEqual(self.myfunc('a', third=None), self.expected)

    def test_exceptions(self):
        self.assert_(issubclass(DeoptionError, TypeError))
        self.assertRaises(TypeError,
            lambda: Optional()
        )
        self.assertRaises(TypeError,
            lambda: Optional(NotPassed, NotPassed)
        )
        
        opt = Optional('a')
        opt.default = NotPassed
        self.assertRaises(DeoptionError,
            lambda: opt.deoption()
        )
        
        self.assertRaises(DeoptionError,
            lambda: deoption(None)
        )
        self.assertRaises(DeoptionError,
            lambda: deoption(None, NotPassed, NotPassed)
        )
        self.assertRaises(DeoptionError,
            lambda: deoption(NotPassed)
        )

if __name__ == "__main__":
    unittest.main()