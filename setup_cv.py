from setuptools import setup
from Cython.Build import cythonize
import numpy

setup(
    ext_modules=cythonize("cross_val.pyx"),
    include_dirs=[numpy.get_include()]
    )