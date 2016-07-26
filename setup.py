#!/usr/bin/env python3

from setuptools import setup

setup(
    name='sht',
    version='1.0',
    description='A fast spherical harmonic transform implementation',
    author='Praveen Venkatesh',
    url='https://github.com/praveenv253/sht',
    packages=['sht', ],
    install_requires=['numpy', 'scipy', 'matplotlib', ],
    setup_requires=['pytest-runner', ],
    tests_require=['pytest', ],
    license='MIT',
)
