"""
The setup package to install Super Framework dependencies and plugins
"""
from setuptools import setup, find_packages
import os
import sys

this_dir = os.path.abspath(os.path.dirname(__file__))
long_description = None
total_description = None
# Get the package version from the framework/__version__.py file
about = {}
with open(os.path.join(
        this_dir, 'framework', '__version__.py'), 'rb') as f:
    exec(f.read().decode('utf-8'), about)

setup(
    name='Super-Framework',
    version=about['__version__'],
    description='The complete web automation library for end-to-end testing.',
    url='https://github.com/zahed3795/Super-Framework',
    platforms=["Windows"],
    author='Zahed Khan',
    author_email='zahed3795@icloud.com',
    maintainer='Zahed Khan',
    license="MIT",
    classifiers=[
        "Development Status :: 1- Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Automation For All",
        "My Word :: Live Free Or Die"," All Life Matters"
        "Intended Audience :: Information Technology,QA",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
        "Programming Language :: Python :: 3.7, 3.8, 3.9, ++",
        "Topic :: Software Testing :: Quality Assurance",
    ],
    python_requires='>=3.7.*, !=3.8.*',
    install_requires=[
        'webdriver_manager==3.2.2',
        'pytest==6.1.1',
        'pytest-xdist==2.1.0',
        'parameterized==0.7.4',
        'cryptography==3.1.1',
        'requests==2.24.0',
        'pytest-json-report==1.2.1',
        'pytest-json==0.4.0',
        'openpyxl==3.0.5',
        'elementpath==2.0.3',
        'pytest-html-reporter==0.2.3',
        'pytest-bdd==4.0.1',
        'pytest-html==2.1.1',
        'numpy==1.19.2',
        'selenium==3.141.0',
        'setuptools>=50.3.2',
        'importlib-metadata == 2.0.0',
        'colorama==0.4.4',
        'urllib3==1.25.11',
        'cssselect==1.1.0',
        'chardet==3.0.4',
        'certifi==2020.6.20',
        'cryptography==3.1.1',
        'pytest-bdd==4.0.1',
        'pytest-bdd-web==0.1.1',
        'zipp==3.3.1',
        'virtualenv>=20.0.35',
        'pymysql==0.10.1',
        'pyopenssl==19.1.0',
        'pytest-rerunfailures==9.1.1',
        'pytest-metadata==1.10.0',
        'pytest-ordering==0.6',
        'pytest-cov==2.10.1',
        'pytest-forked==1.3.0',
        'py==1.9.0',
        'msedge-selenium-tools==3.141.2',
        'soupsieve==2.0.1',
        'beautifulsoup4==4.9.3',
    ],
    packages=[
        'framework',
        'framework.commands',
        'framework.cryption',
        'framework.config',
        'framework.core',
        'framework.drivers',
        'framework.data',
        'framework.fixtures',
        'framework.database',
        'framework.plugins',
        'framework.utilities',

    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'heisenberg = framework.commands.run:main',
            'zahed = framework.commands.run:main',
            'qa = framework.commands.run:main',
        ]
        #,'pytest11': ['framework = framework.plugins.pytest_plugin']
    }
)

print("\n*** Super Framework Installation Complete! ***\n")