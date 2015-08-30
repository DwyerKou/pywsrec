#! /usr/bin/env python
#
# Copyright (C) 2015, WS-DREAM, CUHK
# License: MIT

description = 'pywsrec - A python package to bechmark Web service QoS prediction approaches'

from distutils.core import setup, Extension
# from setuptools import setup, find_packages
import os
import os.path
import numpy
from distutils.sysconfig import *
# from distutils.util import *

try:
   from distutils.command.build_py import build_py_2to3 \
       as build_py
except ImportError:
   from distutils.command.build_py import build_py

try:
   from Cython.Distutils import build_ext
except ImportError:
   use_cython = False
else:
   use_cython = True

extra_compile_args = ['-O2']

#### data files
data_files = []

#### scripts
scripts = []

#### Python include
py_inc = [get_python_inc()]

#### NumPy include
# np_lib = os.path.dirname(numpy.__file__)
np_inc = [numpy.get_include()]

#### cmdclass
cmdclass = {'build_py': build_py}

#### Extension modules
ext_modules = []
if use_cython:
    cmdclass.update({'build_ext': build_ext})
    ext_modules += [Extension("pywsrec.PPCF.P_PMF", 
                              ["pywsrec/PPCF/P_PMF/cP_PMF.cpp",
                              "pywsrec/PPCF/P_PMF/P_PMF.pyx"],
                              language='c++',
                              include_dirs=py_inc + np_inc),
                    Extension("pywsrec.PPCF.P_UIPCC", 
                              ["pywsrec/PPCF/P_UIPCC/cP_UIPCC.cpp",
                              "pywsrec/PPCF/P_UIPCC/P_UIPCC.pyx"],
                              language='c++',
                              include_dirs=py_inc + np_inc)
                              ]

else:
    ext_modules += [Extension("pywsrec.PPCF.P_PMF", 
                              ["pywsrec/PPCF/P_PMF/cP_PMF.cpp",
                              "pywsrec/PPCF/P_PMF/P_PMF.cpp"],
                              include_dirs=py_inc + np_inc),
                    Extension("pywsrec.PPCF.P_UIPCC", 
                              ["pywsrec/PPCF/P_UIPCC/cP_UIPCC.cpp",
                              "pywsrec/PPCF/P_UIPCC/P_UIPCC.cpp"],
                              include_dirs=py_inc + np_inc)
                              ]

packages=['pywsrec', 'pywsrec.PPCF']

classifiers = ['Development Status :: 5 - Production/Stable',
               'Intended Audience :: Science/Research',
               'License :: OSI Approved :: GNU General Public License (GPL)',
               'Programming Language :: C++',
               'Programming Language :: Python',
               'Topic :: Scientific/Engineering :: Artificial Intelligence',
               'Topic :: Scientific/Engineering :: Mathematics',
               'Operating System :: POSIX :: Linux',
               'Operating System :: POSIX :: BSD',
               'Operating System :: MacOS',
               'Operating System :: Microsoft :: Windows',
               'Operating System :: POSIX'
               ]

setup(name = 'pywsrec',
      version='1.0',
      requires=['numpy (>=1.8.1)', 'scipy (>=0.13.3)'],
      description=description,
      author='WS-DREAM',
      author_email='wsdream.maillist@gmail.com',
      packages=packages,#find_packages(exclude=['tests*']),
      url='https://wsdream.github.io',
      download_url='https://sourceforge.net/projects/mlpy/',
      license='MIT',
      classifiers=classifiers,
      cmdclass=cmdclass,
      ext_modules=ext_modules,
      scripts=scripts,
      data_files=data_files
      )

print('==============================================')
print('Setup succeeded!\n')

