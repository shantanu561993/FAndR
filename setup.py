#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

setup(
    name='FAR',
    version='0.1.0',
    description="This project will find text in files and replace the text",
    long_description=readme + '\n\n' + history,
    author="Shantanu Khandelwal",
    author_email='shantanu561993@gmail.com',
    url='https://github.com/shantanu561993/FAR',
    packages=[
        'FAR',
    ],
    package_dir={'FindAndReplace':
                 'FindAndReplace'},
    include_package_data=True,
    license="GPLv3+",
    zip_safe=False,
    keywords='FAR',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    #test_suite='tests',
    #tests_require=test_requirements
)
