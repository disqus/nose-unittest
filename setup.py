#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='nose-unittest',
    version='0.1.0',
    author='DISQUS',
    author_email='opensource@disqus.com',
    url='http://github.com/disqus/nose-unittest',
    packages=find_packages(exclude=["tests"]),
    zip_safe=False,
    install_requires=[
        'nose>=0.9',
    ],
    entry_points={
       'nose.plugins.0.10': [
            'nose_unittest = nose_unittest:UnitTestPlugin'
        ]
    },
    license='Apache License 2.0',
    include_package_data=True,
)
