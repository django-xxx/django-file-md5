# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.0.1'


setup(
    name='django-file-md5',
    version=version,
    keywords='Django File Md5',
    description='Django File Md5',
    long_description=open('README.rst').read(),

    url='https://github.com/django-xxx/django-file-md5',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=['filemd5'],
    py_modules=[],
    install_requires=[],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
    ],
)
