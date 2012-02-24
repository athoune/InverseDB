#!/usr/bin/env python

from setuptools import setup

# http://pypi.python.org/pypi?%3Aaction=list_classifiers

setup(name='inversedb',
    version='0.1',
    package_dir={'': 'src'},
    url='http://github.com/athoune/InverseDB',
    #scripts=[],
    description="Column oriented experimental database",
    long_description="""
Build upon classical key/value database like GBM, KyotoCabinet or LevelDB.
Inverse reference use bitset for simple and efficient boolean queries.
""",
    classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Operating System :: POSIX',
          'Operating System :: MacOS :: MacOS X',
          'Programming Language :: Python',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: French',
          'Topic :: Database :: Database Engines/Servers'
        ],
    license="MIT",
    author="Mathieu Lecarme",
    packages=['inversedb'],
    keywords= ["database", "bitset"],
    zip_safe = True,
    install_requires=["intbitset"],
)

