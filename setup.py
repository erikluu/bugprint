from setuptools import setup, find_packages

setup(
    name='bug_print',
    version='0.1',
    packages=find_packages(),
    description="A package to print to the console for all your bug fixin' needs.",
    author='Erik Luu',
    author_email='eeluu19@gmail.com',
    url='https://github.com/erikluu',
    license='MIT',
    install_requires=[
        'inspect',
        'os'
    ],
)
