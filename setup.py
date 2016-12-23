from setuptools import setup
import os

if not os.path.isfile("README.rst"):
    raise RuntimeError("Generate README.rst from README.md before running tox or setup")

with open('./README.rst') as fd:
    long_description = fd.read()

setup(
    name='pytest-finer-verdicts',
    packages=['pytest_finer_verdicts'],
    version='1.0.3',
    description='A pytest plugin to treat non-assertion failures as test errors.',
    long_description=long_description,
    author='Venkatesh-Prasad Ranganath',
    license='BSD 3-Clause License',
    platforms=['unix', 'linux', 'osx', 'cygwin', 'win32'],
    keywords=['testing', 'pytest', 'verdict'],
    install_requires=['pytest>=2.9'],
    download_url='https://github.com/rvprasad/pytest-finer-verdicts/archive/v1.0.3.zip',
    url='https://github.com/rvprasad/pytest-finer-verdicts',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    # the following makes a plugin available to py.test
    entry_points={'pytest11': ['finer_verdicts = pytest_finer_verdicts.plugin']}
)
