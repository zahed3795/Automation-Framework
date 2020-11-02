"""A test library for string manipulation and verification"""
import re

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


def isinstance(x, A_tuple):  # real signature unknown; restored from __doc__
    """
    Return whether an object is an instance of a class or of a subclass thereof.

    A tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the target to
    check against. This is equivalent to ``isinstance(x, A) or isinstance(x, B)
    or ...`` etc.
    """
    pass
def is_string(item):
    # Returns False with `b'bytes'` on IronPython on purpose. Results of
    # `isinstance(item, basestring)` would depend on IronPython 2.7.x version.
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