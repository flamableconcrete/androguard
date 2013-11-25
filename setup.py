#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = 'androguard',
    version = '1.9.1',
    packages = find_packages(),
    scripts = ['androaxml.py', 'androcsign.py', 'androdiff.py', 'androgexf.py',
               'androlyze.py', 'andromercury.py', 'androrisk.py', 'androsign.py',
               'androsim.py', 'androxgmml.py', 'apkviewer.py',
               'androdd.py', 'androapkinfo.py',
               ],
    install_requires=[
        'distribute',
        'ipython',   # androlyze.py
        'pygments',  # androlyze.py
        'pydot',     # androdd.py
        'ptrace',    # androdump.py
        'pyfuzzy',   # androrisk.py
        #'cython',    # sparsehash, because it won't download automatically
        #'sparsehash' # elsim
        ],
)
