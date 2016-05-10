from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pindrop-sysmonitor',

    version='0.0.1',

    description='Monitors system and provides output through RESTful API',
    long_description=long_description,

    url='https://github.com/jpopesculian/pindrop-sysmonitor',

    author='Julian Popescu',
    author_email='jpopesculian@gmail.com',

    license='MIT',

    install_requires=[
        'Flask',
        'inflection'
    ],

    entry_points={
        'console_scripts': [
            'sysmonitor=sysmonitor.__main__:main',
        ],
    },
)