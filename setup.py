# -*- coding: utf-8 -*-

from setuptools import setup

project = "tumblr"

setup(
    name=project,
    version='0.1',
    url='https://github.com/ahsanali/tumblr-theme',
    description='Tumblr-Theme is an applicaton to edit tumblr theme without using their web UI',
    author='Muhammad Ahsan Ali',
    author_email='sn.ahsanali@gmail.com',
    packages=["tumblr"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'Flask-Script',
        'tornado',
        'psycopg2'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries'
    ]
)
