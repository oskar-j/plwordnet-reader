import setuptools
from plwordnet.version import Version


setuptools.setup(name='plwordnet',
                 version=Version('0.1.0').number,
                 description='Library for reading information from Polish wordnet',
                 long_description=open('README.md').read().strip(),
                 author='Oskar Jarczyk',
                 author_email='oskar.jarczyk@gmail.com',
                 url='http://path-to-my-packagename',
                 py_modules=['packagename'],
                 install_requires=[],
                 license='MIT License',
                 zip_safe=False,
                 keywords='wordnet pl-wordnet python nlp',
                 classifiers=['Packages', ])
