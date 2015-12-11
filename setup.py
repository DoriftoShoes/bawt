import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "bawt",
    version = "0.0.1",
    author = "DoriftoShoes",
    author_email = "self@dorifto.shoes",
    description = ("Garage/hydroponics controller project "),
    license = "Apache",
    keywords = "hydroponics",
    url = "https://github.com/DoriftoShoes/bawt",
    packages=['bawt', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
    ],
    entry_points={
        'console_scripts': [
            'bawtd = bawt.bin.daemon:main'
        ]
    }
)
