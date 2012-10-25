#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='nose-unittest',
    version='0.1.1',
    author='DISQUS',
    author_email='opensource@disqus.com',
    url='http://github.com/disqus/nose-unittest',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    zip_safe=False,
    install_requires=[
        'nose>=0.9',
    ],
    entry_points={
       'nose.plugins.0.10': [
            'nose_unittest = nose_unittest.plugin:UnitTestPlugin'
        ]
    },
    license='Apache License 2.0',
    include_package_data=True,
)
