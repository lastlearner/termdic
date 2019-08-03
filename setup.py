# coding: utf-8

from setuptools import setup, find_packages

version = '0.1.3'

setup(
    name = 'termdic',
    version = version,
    author = 'lastlearner',
    author_mail = '429825736@qq.com',
    url = 'https://github.com/lastlearner/termdic',
    description = 'Dictionary in your terminal',
    keywords = 'dictionary, terminal',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    install_requires = [
        'requests',
        'termcolor',
    ],
    entry_points = {
        'console_scripts': [
            'tdic = termdic.termdic:main'
        ]
    },
)
