
from codecs import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'VERSION'), encoding='utf-8') as f:
    version = f.read()


setup(
    name='econopy', version=version,
    description='Simple economic utilities',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/KeoH/econoPy',
    author='Francisco Manzano Magaña',
    author_email='keoh77@gmail.com',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Office/Business :: Financial :: Accounting',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    keywords='economic,financial,business,accounting',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    project_urls={
        'Bug Reports': 'https://github.com/KeoH/econoPy/issues',
        'Source': 'https://github.com/KeoH/econoPy/',
    },
)
