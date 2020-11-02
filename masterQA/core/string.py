"""A test library for string manipulation and verification"""
import re
from random import randint
from string import ascii_lowercase, ascii_uppercase, digits

TRUE_STRINGS = {'TRUE', 'YES', 'ON', '1'}
FALSE_STRINGS = {'FALSE', 'NO', 'OFF', '0', 'NONE', ''}


def lower(string):
    return string.lower()


def upper(string):
    return string.upper()


def _convert_to_index(value, name):
    if value == '':
        return 0
    if value is None:
        return None
    return _convert_to_integer(value, name)


def _convert_to_integer(value, name):
    try:
        return int(value)
    except ValueError:
        raise ValueError("Cannot convert '%s' argument '%s' to an integer."
                         % (name, value))

def isinstance(x, A_tuple):
  pass


def is_string(item):
    return isinstance(item, (str, 'string'))


def is_truthy(item):
    """Returns `True` or `False` depending is the item considered true or not.
    """
    if is_string(item):
        return item.upper() not in FALSE_STRINGS
    return bool(item)


class StringBase:

    def convert_to_lower_case(self, string):
        return lower("\n" + str(string))

    def convert_to_upper_case(self, string):
        return upper("\n" + str(string))

    def get_line_count(self, string):
        """Returns and logs the number of lines in the given string."""
        count = len(string.splitlines())
        return count

    def split_to_lines(self, string, start=0, end=None):
        """Splits the given string to lines"""
        start = _convert_to_index(start, 'start')
        end = _convert_to_index(end, 'end')
        lines = string.splitlines()[start:end]
        return lines

    def get_line(self, string, line_number):
        """Returns the specified line from the given ``string``."""
        line_number = _convert_to_integer(line_number, 'line_number')
        return string.splitlines()[line_number]

    def get_lines_containing_string(self, string, pattern, case_insensitive=False):
        """Returns lines of the given ``string`` that contain the ``pattern``.
        """
        if is_truthy(case_insensitive):
            pattern = pattern.lower()
            contains = lambda line: pattern in line.lower()
        else:
            contains = lambda line: pattern in line
        return self._get_matching_lines(string, contains)

    def _get_matching_lines(self, string, matches):
        lines = string.splitlines()
        matching = [line for line in lines if matches(line)]
        return '\n'.join(matching)

    def get_regexp_matches(self, string, pattern, *groups):
        """Returns a list of all non-overlapping matches in the given string
        Examples: get_regexp_matches('the string','xxx')
        """
        regexp = re.compile(pattern)
        groups = [self._parse_group(g) for g in groups]
        return [m.group(*groups) for m in regexp.finditer(string)]

    def _parse_group(self, group):
        try:
            return int(group)
        except ValueError:
            return group

    def replace_string(self, string, search_for, replace_with, count=-1):
        """Replaces ``search_for`` in the given ``string`` with ``replace_with``.
        Examples: self.replace_string('Hello_world!','In_god_we_trust')
        """
        count = _convert_to_integer(count, 'count')
        return string.replace(search_for, replace_with, count)

    def replace_string_using_regexp(self, string, pattern, replace_with, count=-1):
        """Replaces ``pattern`` in the given ``string`` with ``replace_with``.
            Replace String Using Regexp | ${str} | (Hello|Hi) | ${EMPTY} | count=1 |
        """
        count = _convert_to_integer(count, 'count')
        # re.sub handles 0 and negative counts differently than string.replace
        if count == 0:
            return string
        return re.sub(pattern, replace_with, string, max(count, 0))

    def remove_string(self, string, *removables):
        """Removes all ``removables`` from the given ``string``"""
        for removable in removables:
            string = self.replace_string(string, removable, '')
        return string

    def split_string(self, string, separator=None, max_split=-1):
        """Splits the ``string`` using ``separator`` as a delimiter string."""
        if separator == '':
            separator = None
        max_split = _convert_to_integer(max_split, 'max_split')
        return string.split(separator, max_split)

    def split_string_from_right(self, string, separator=None, max_split=-1):
        """Splits the ``string`` using ``separator`` starting from right."""
        if separator == '':
            separator = None
        max_split = _convert_to_integer(max_split, 'max_split')
        return string.rsplit(separator, max_split)

    def split_string_to_characters(self, string):
        """Splits the given ``string`` to characters."""
        return list(string)

    def fetch_from_left(self, string, marker):
        """Returns contents of the ``string`` before the first occurrence of ``marker``."""
        return string.split(marker)[0]

    def fetch_from_right(self, string, marker):
        """Returns contents of the ``string`` after the last occurrence of ``marker``."""
        return string.split(marker)[-1]

    def generate_random_string(self, length=8, chars='[LETTERS][NUMBERS]'):
        """Generates a string with a desired ``length`` from the given ``chars``."""
        if length == '':
            length = 8
        length = _convert_to_integer(length, 'length')
        for name, value in [('[LOWER]', ascii_lowercase),
                            ('[UPPER]', ascii_uppercase),
                            ('[LETTERS]', ascii_lowercase + ascii_uppercase),
                            ('[NUMBERS]', digits)]:
            chars = chars.replace(name, value)
        maxi = len(chars) - 1
        return ''.join(chars[randint(0, maxi)] for _ in range(length))

    def get_substring(self, string, start, end=None):
        """Returns a substring from ``start`` index to ``end`` index."""
        start = _convert_to_index(start, 'start')
        end = _convert_to_index(end, 'end')
        return string[start:end]

    def strip_string(self, string, mode='both', characters=None):
        """Remove leading and/or trailing whitespaces from the given string."""
        try:
            method = {'BOTH': string.strip,
                      'LEFT': string.lstrip,
                      'RIGHT': string.rstrip,
                      'NONE': lambda characters: string}[mode.upper()]
        except KeyError:
            raise ValueError("Invalid mode '%s'." % mode)
        return method(characters)

    def should_be_lowercase(self, string, msg=None):
        """Fails if the given ``string`` is not in lowercase."""
        if not string.islower():
            return False

    def should_be_uppercase(self, string):
        """Fails if the given ``string`` is not in uppercase."""
        if not string.isupper():
            return False

    def should_be_titlecase(self, string, msg=None):
        """Fails if given ``string`` is not title."""
        if not string.istitle():
            return False
