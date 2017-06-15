"""pytest-env setup module."""

from setuptools import setup

DESCRIPTION = 'py.test plugin that allows you to add environment variables.'

setup(
    name='pytest-env',
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    version='0.6.2',
    author='dev@mobile-dynasty.com',
    author_email='dev@mobile-dynasty.com',
    url='https://github.com/MobileDynasty/pytest-env',
    packages=['pytest_env'],
    entry_points={'pytest11': ['env = pytest_env.plugin']},
    install_requires=['pytest>=2.6.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ]
)
