"""
The setup package to install Super Framework dependencies and plugins
"""

from setuptools import setup, find_packages
import os
import sys


__version__ = 1.0
setup(
    name='Super-Framework',
    version=__version__,
    description='The complete web automation library for end-to-end testing.',
    url='https://github.com/zahed3795/Super-Framework',
    platforms=["Windows", "Linux", "Mac OS-X"],
    author='Zahed Khan',
    author_email='zahed3795@icloud.com',
    maintainer='Zahed Khan',
    license="MIT",
    classifiers=[
        "Development Status :: 1- Production/Stable",
        "Environment :: Console",
        "Environment :: MS Windows",
        "Environment :: Web Environment",
        "Framework :: Automation For All",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7, 3.8, 3.9, ++",
        "Topic :: Software Testing :: Quality Assurance",
    ],
    python_requires='>=!=3.7.*',
    install_requires=[
        'pip>=20.2.4',
        'packaging>=20.4',
        'setuptools>=50.3.2',
        'setuptools-scm',
        'wheel>=0.35.1',
        'six',
        'nose',
        'ipdb',
        'parso==0.7.1',
        'jedi==0.17.2',
        'idna==2.10',
        'chardet==3.0.4',
        'urllib3==1.25.11',
        'requests==2.24.0',
        'selenium==3.141.0',
        'msedge-selenium-tools==3.141.2',
        'more-itertools==8.6.0',
        'cssselect==1.1.0',
        'pluggy==0.13.1',
        'attrs>=20.2.0',
        'py==1.9.0',
        'pytest==6.1.2',
        'pytest-cov==2.10.1',
        'pytest-forked==1.3.0',
        'pytest-html==2.0.1',
        'pytest-metadata==1.10.0',
        'pytest-ordering==0.6',
        'pytest-rerunfailures==9.1.1',
        'pytest-xdist==2.1.0',
        'parameterized==0.7.4',
        'soupsieve==2.0.1',
        'beautifulsoup4==4.9.3',
        'cryptography==3.2.1',
        'pyopenssl==19.1.0',
        'pygments==2.7.2',
        'traitlets==5.0.5',
        'prompt-toolkit==3.0.8',
        'ipython==7.19.0',
        'colorama==0.4.4',
        'importlib-metadata==2.0.0',
        'virtualenv>=20.1.0',
        'pymysql==0.10.1',
        'coverage==5.3',
        'brython==3.9.0',
        'pyotp==2.4.1',
        'boto==2.49.0',
        'cffi==1.14.3',
        'rich==9.1.0',
        'zipp==3.4.0',
        'flake8==3.8.4',
        'pyflakes==2.2.0',
        'tornado==6.1',
        'certifi>=2020.6.20',
        'allure-pytest==2.8.19',
        'pdfminer.six==20201018',
    ],
    packages=[
        'masterQA',
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'masterQA = masterQA.console_scripts.run:main',
            'sdet = masterQA.console_scripts.run:main',
            'qa = masterQA.console_scripts.run:main',
        ],
        'pytest11': ['masterQA = masterQA.plugins.pytest_plugin']
    }
)

print("\n*** Super Framework Installation Complete! ***\n")
