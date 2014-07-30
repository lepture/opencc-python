#!/usr/bin/env python
# coding: utf-8


try:
    # python setup.py test
    import multiprocessing
except ImportError:
    pass

from setuptools import setup
import opencc


def fread(filepath):
    with open(filepath, 'r') as f:
        return f.read()

setup(
    name='OpenCC',
    version=opencc.__version__,
    url='https://github.com/lepture/opencc-python',
    author='Hsiaoming Yang',
    author_email='me@lepture.com',
    description='A ctypes-based OpenCC converter for Chinese.',
    long_description=fread('README.rst'),
    license='BSD',
    packages=['opencc'],
    zip_safe=False,
    platforms='any',
    tests_require=['nose'],
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
