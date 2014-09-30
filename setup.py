from setuptools import setup


setup(
    name='optional',
    version=open('VERSION').read().strip(),
    author='Oakland John Peters',
    author_email='oakland.peters@gmail.com',
    description=(
        "A simple implementation of an 'Optional' data type. "
        "Optional is an alternative to passing around 'None', in cases where "
        "'None' might be normally be passed in for that parameter. "
        "Heavily inspired by Rust's 'Option'  and Haskell's 'Maybe' types."
    ),
    long_description=open('README.rst').read(),
    url='http://bitbucket.org/OPeters/optional/',
    license='MIT',
    packages=['optional'],

    classifiers=[
        #'Development Status :: 5 - Production/Stable',
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: Implementation :: CPython',

        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Topic :: Utilities'
    ]
)
