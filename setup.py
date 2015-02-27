#!/usr/bin/env python
# -*- coding: utf8 -*-

from setuptools import setup, find_packages


setup(
    name='zabbix_kato',
    author='dsociative',
    author_email='admin@geektech.ru',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'zabbix_kato = zabbix_kato.notify:main',
        ]
    },
    install_requires=[
        'sh'
    ]
)
