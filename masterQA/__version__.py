# Super-Framework package
__version__ = "1a.0bc.0.dev"

import re
import sys

# Version number typically updated by running `invoke set-version <version>`.
# Run `invoke --help set-version` or see tasks.py for details.
VERSION = '4.0a3.dev1'


def get_version(naked=False):
    if naked:
        return re.split('(a|b|rc|.dev)', VERSION)[0]
    return VERSION


print(VERSION)


def get_full_version(program=None, naked=False):
    version = '%s %s (%s %s on %s)' % (program or '',
                                       get_version(naked),
                                       get_interpreter(),
                                       sys.version.split()[0],
                                       sys.platform)
    return version.strip()


def get_interpreter():
    if sys.platform.startswith('java'):
        return 'Jython'
    if sys.platform == 'cli':
        return 'IronPython'
    if 'PyPy' in sys.version:
        return 'PyPy'
    return 'Python'

