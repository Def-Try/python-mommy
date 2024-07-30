from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='pythonmommy',
    version='0.1.3',
    author='googer',
    author_email='googer760@gmail.com',
    description='Mommy\'s here to support you when running python~ ❤️',
    long_description=(Path(__file__).parent/"README.md").read_text(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'colorama',
        'termcolor'
    ],
    python_requires='>=3.9',
)
