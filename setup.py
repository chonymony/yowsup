#!/usr/bin/env python
from __future__ import print_function
from setuptools import setup, find_packages
import yowsup
import platform
import sys

deps = ['consonance==0.1.5', 'argparse', 'python-axolotl==0.2.2', 'six==1.10', 'appdirs', 'protobuf>=3.6.0']

if sys.version_info < (2, 7):
    deps.append('importlib')

if platform.system().lower() == "windows":
    deps.append('pyreadline')
else:
    try:
        import readline
    except ImportError:
        import pyreadline as readline

setup(
    name='yowsup',
    version=yowsup.__version__,
    url='http://github.com/tgalal/yowsup/',
    license='GPL-3+',
    author='Tarek Galal',
    tests_require=[],
    install_requires = deps,
    scripts = ['yowsup-cli'],
    #cmdclass={'test': PyTest},
    author_email='tare2.galal@gmail.com',
    description='The WhatsApp lib',
    #long_description=long_description,
    packages= find_packages(),
    include_package_data=True,
    data_files = [('yowsup/common', ['yowsup/common/mime.types'])],
    platforms='any',
    #test_suite='',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        #'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ],
    #extras_require={
    #    'testing': ['pytest'],
    #}
)
