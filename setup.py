from setuptools import setup

setup(
    name='pytest-finer-verdicts',
    packages=['pytest_finer_verdicts'],
    version='1.0.1',
    description='A pytest plugin to treat non-assertion failures as test errors.',
    author='Venkatesh-Prasad Ranganath',
    license='BSD 3-Clause License',
    keywords=['testing', 'pytest', 'verdict'],
    install_requires=['pytest>=2.9'],
    download_url='https://github.com/rvprasad/pytest-finer-verdicts/archive/v1.0.1.zip',
    url='https://github.com/rvprasad/pytest-finer-verdicts',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
    ],
    # the following makes a plugin available to py.test
    entry_points={'pytest11': ['finer_verdicts = pytest_finer_verdicts.plugin']}
)
