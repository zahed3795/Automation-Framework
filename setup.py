"""
The setup package to install Super-Framework dependencies and plugins
(Uses selenium 3.x)
"""

from setuptools import setup, find_packages  #
import os
import sys


this_dir = os.path.abspath(os.path.dirname(__file__))
print(this_dir)
long_description = None
total_description = None
about = {}
# Get the package version from the mastorQA/__version__.py file
with open(os.path.join(
        this_dir, 'masterQA', '__version__.py'), 'rb') as f:
    exec(f.read().decode('utf-8'), about)

flake8_status = os.system("flake8 --exclude=temp")
if flake8_status != 0:
    print("\nWARNING! Fix flake8 issues before publishing!\n")
    sys.exit()


setup(
    name='mastorQA',
    version=about['__version__'],
    description='A complete framework for End to End testing ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/zahed3795/Super-Framework.git',
    platforms=["Windows"],
    author='Zahed Khan',
    author_email='zahedkhan3795@gmail.com',
    maintainer='Zahed Khan',
    license="MIT",
    classifiers=[
        "Development Status :: 1 - Production/Stable",
        "Environment :: Console",
        "Environment :: Win32 (MS Windows)",
        "Environment :: Web Environment",
        "Framework :: Super",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Testing :: Acceptance",
        "Topic :: Software Development :: Testing :: Traffic Generation",
        "Topic :: Utilities",
    ],
    python_requires='>==3.7.* ,!=3.8.*, !=3.9.*',
    install_requires=[
        'webdriver_manager==3.2.2',
        'pytest==6.1.1',
        'pytest-xdist==2.1.0;',
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
        'setuptools-scm',
        'setuptools>=44.1.1',
        'importlib-metadata == 2.0.0',
        'colorama==0.4.4',
        'urllib3=1.25.11',
        'cssselect==1.1.0',
        'chardet==3.0.4',
        'certifi==2020.6.20',
        'cryptography==3.1.1',
        'pytest-bdd==4.0.1',
        'pytest-bdd-web==0.1.1',
        'zipp==3.3.1;python_version',
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
        'beautifulsoup4==4.9.3'

    ],
    packages=[
        'mastorQA',
        'mastorQA.common',
        'mastorQA.config',
        'mastorQA.core',
        'mastorQA.data',
        'mastorQA.database',
        'mastorQA.driver',
        'mastorQA.fixtures',
        'mastorQA.requests',
        'mastorQA.utilities',

    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'mastorQA = mastorQA.console_scripts.run:main',
            'qa = mastorQA.console_scripts.run:main',  # Simplified name
        ],

    }
)

# print(os.system("cat mastorQA.egg-info/PKG-INFO"))
print("\n*** Installation Complete! ***\n")
