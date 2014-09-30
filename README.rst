Optional
=============

Overview
---------
Optional is a Python package inspired by Rust's `Option <http://doc.rust-lang.org/std/option/>`_ and Haskell's `Maybe <https://hackage.haskell.org/package/base-4.2.0.1/docs/Data-Maybe.html/>`_.
It correctly distinguishes the different variation's of `None` that can be passed into a function. Specifically, `Optional` makes it easy to distinguish `No-value-was-passed` from the value `None` being passed.
It also enhances specify default argument values, in a way that removes some `common error cases <http://docs.python-guide.org/en/latest/writing/gotchas//>`_.


Examples
--------
`Optional` is used as the value of a optional argument, in cases where `None` is also a valid input for that argument (common in meta-programming related functions).

.. code:: python

	from optional import Optional, deoption
	
	def attrgetter(obj, index, default=Optional()):
		try:
			return getattr(obj, index)
		except AttributeError:
			if isinstance(default, Optional


`Optional` also handles a common Python error stemming from mutable default arguments.

.. code::python
	# Incorrect on repeated application
	def append(elm, target=[]):
		target.append(elm)
		return elm
	
	#Correct
	def append(elm, target=Optional(execute=list)):
		target.append(elm)
		return elm

Further, the `Optional` package also provides a base class `NullType` which is considered to be a parent class to `Optional`, `None`, and `NotPassed`.

NullType

NotPassed
NotPassedType

Optional
deoption


Installation
-------------

.. code::python

	pip install optional


License
-----------
The MIT License (MIT)

Copyright (C) 2014, Oakland John Peters.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
