Optional
=============

Overview
---------
Optional is a Python package inspired by `Rust's <http://doc.rust-lang.org/std/option/>`_ ``Option``  and `Haskell's <https://hackage.haskell.org/package/base-4.2.0.1/docs/Data-Maybe.html/>`_ ``Maybe``.
It correctly distinguishes the different variation's of ``None`` that can be passed into a function. Specifically, ``Optional`` makes it easy to distinguish ``No-value-was-passed`` (called ``NotPassed`` in this package) from the value ``None`` being passed.
It also enhances the ability to specify default argument values, in a way that removes some `common error cases <http://docs.python-guide.org/en/latest/writing/gotchas//>`_.


Examples
--------
``Optional`` is primarily used as the default value of a optional argument, in cases where ``None`` is also a valid input for that argument. This is commonly encountered in meta-programming related functions. For example:

.. code:: python

	from optional import Optional
	
	def attrgetter(obj, index, default=Optional()):
		try:
			return getattr(obj, index)
		except AttributeError:
			if isinstance(default, Optional)

``Optional`` also handles a common Python error stemming from mutable default arguments, via the ``deoption`` function:

.. code:: python
	
	def append(elm, target=[]):
		target.append(elm)
		return elm

	def append(elm, target=Optional(execute=list)):
		target = deoption(target)
		target.append(elm)
		return elm

Further, the ``Optional`` package also provides a base class's to distinguish common argument cases. ``NotPassedType`` is an ancestral type for both ``NotPassed`` and ``Optional``, but *not* ``None``. ``NullType`` is considered to be an ancester class for all three.

.. code:: python

	from optional import NullType, Optional, NotPassed, NotPassedType
	assert isinstance(None, NullType)
	assert isinstance(Optional(), NullType)
	assert isinstance(NotPassed, NullType)

	assert not isinstance(None, NotPassedType)
	assert isinstance(Optional(), NotPassedType)
	assert isinstance(NotPassed, NotPassedType)
	

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
