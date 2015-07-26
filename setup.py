"""gybote, the twitter bot."""

from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gybote',
    version='1.2.0',
    description='a twitter bot that tweets godspeed you! black emperor lyrics.',
    long_description=long_description,
    url='https://github.com/joshuarichard/gybote',
    author='joshua richard',
    author_email='eos.josh.richard@gmail.com',
    license='Apache 2.0',
    classifiers=[
        'Development Stats :: 3 - Alpha',
        'Intended Audience :: Humans',
        'Topic :: Twitter :: Bot',
        'License :: OSI Approved :: Apache 2.0',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='godspeed you black emperor twitter bot',
    install_requires=['tweepy'],
)