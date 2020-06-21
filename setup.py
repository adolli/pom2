# coding=utf-8
from setuptools import setup, find_packages


def parse_requirements(filename='requirements.txt'):
    """ load requirements from a pip requirements file. (replacing from pip.req import parse_requirements)"""
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


setup(
    name='pom',
    version='1.0.0',
    keywords="game, pom, eiyuu densetsu, sen no kiseki, The Legend of Heroes",
    description='A game, pom.',
    long_description='A game, pom.',
    packages=find_packages(),
    include_package_data=True,
    install_requires=parse_requirements(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

    author='adolli',
    author_email='adolli@163.com',
)
