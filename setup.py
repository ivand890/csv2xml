from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='csv2xml',
    version='0.0.1',
    description='Simplest converter csv to xml',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ivand890/csv2xml',
    author='Ivan Delgado de la Paz',
    author_email='ivand890@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Markup :: XML',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
    ],
    keywords='text processing markup xml csv converter',
    packages=find_packages(), 
    python_requires='>=3.5',
    install_requires=['peppercorn'],  # TODO
    entry_points={
        'console_scripts': [
            'csv2xml=csv2xml:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/ivand890/csv2xml/issues',
        'Source': 'https://github.com/ivand890/csv2xml',
    },
)