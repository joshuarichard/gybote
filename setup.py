"""gybote, a twitter bot."""

from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gybote',
    packages=['gybote'],
    version='0.0.3',
    description='a twitter bot that tweets godspeed you! black emperor lyrics.',
    long_description=long_description,
    url='https://github.com/joshuarichard/gybote',
    author='Joshua Richard',
    author_email='eos.josh.richard@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Communications',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords=['godspeed you black emperor', 'twitter', 'bot', 'fun'],
    install_requires=['tweepy'],
)
