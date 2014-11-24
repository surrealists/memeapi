#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'memeapi',
]

requires = ['requests>=2.1.0']

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='memeapi',
    version='0.2.3',
    description='Tiny wrapper over memegenerator.net API.',
    author='Cristian Cabrera',
    author_email='surrealcristian@gmail.com',
    url='https://github.com/surrealists/memeapi',
    packages=packages,
    package_dir={'memeapi': 'memeapi'},
    include_package_data=True,
    install_requires=requires,
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
)
