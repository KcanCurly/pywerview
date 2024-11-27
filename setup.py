#!/usr/bin/env python3

from setuptools import setup, find_packages

long_description = open('README.md').read()

setup(
    name='pywerview',
    version='0.7.1',
    description='A Python port of PowerSploit\'s PowerView',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.6',
        'Topic :: Security',
    ],
    install_requires=[
        "impacket @ git+https://github.com/fortra/impacket@db71504529008bdbdd900549f6e4293be2e32c88#egg=impacket",
        "beautifulsoup4",
        "lxml",
        "pyasn1",
        "ldap3-bleeding-edge",
        "gssapi",
        "pycryptodome"
    ],
    keywords='python powersploit pentesting recon active directory windows',
    url='https://github.com/the-useless-one/pywerview',
    author='Yannick Méheut',
    author_email='yannick@meheut.org',
    license='GNU GPLv3',
    packages=find_packages(include=[
        "pywerview", "pywerview.*"
    ]),
    entry_points = {
        'console_scripts': ['pywerview=pywerview.cli.main:main'],
    },
    zip_safe=False
)